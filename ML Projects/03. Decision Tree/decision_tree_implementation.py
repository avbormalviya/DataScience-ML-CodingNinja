from collections import Counter
import numpy as np
from graphviz import Digraph
import colorsys


class DecisionTreeClassifier:
    def __init__(self, max_depth=None):
        # Initialize the decision tree with a max depth limit
        self.__max_depth = max_depth
        self.__tree = None
        self.__feature_names = None
        self.__feature_types = None
        self.__class_names = None
        self.__class_colors = None

    @staticmethod
    def is_continuous(feature_column):
        return np.issubdtype(feature_column.dtype, np.number) and len(np.unique(feature_column)) > 10

    def __full_class_counts(self, y):
        # Always returns full class count list [count_for_class_0, count_for_class_1, ...]
        counts = [0] * len(self.__class_names)
        for label in y:
            counts[label] += 1
        return counts

    def __assign_class_colors(self, n):
        # Return n distinct pastel colors
        return [
            "#{:02x}{:02x}{:02x}".format(
                *[int(c * 255) for c in colorsys.hls_to_rgb(i / n, 0.85, 0.6)]
            )
            for i in range(n)
        ]

    def __entropy(self, y):
        # Calculate the entropy of the target labels (y)
        count = Counter(y)
        total = len(y)
        entropy = 0.0
        for label, cnt in count.items():
            prob = cnt / total  # Calculate the probability of each label
            entropy -= prob * np.log2(prob)  # Sum up entropy values

        return entropy

    def __information_gain(self, x, y, feature):
        # Calculate the information gain for a given feature
        total = len(y)
        base_entropy = self.__entropy(y)  # Entropy before split

        values = set(x[:, feature])  # Get unique values for the feature
        feature_entropy = 0.0

        for value in values:
            subset_y = y[x[:, feature] == value]  # Get subset of target labels for a feature value
            prob = len(subset_y) / total  # Probability of this subset
            feature_entropy += prob * self.__entropy(subset_y)  # Entropy of this subset

        return base_entropy - feature_entropy  # Information gain

    def __split_information(self, x, feature):
        # Calculate the split information (used in Gain Ratio) for a feature
        count = Counter(x[:, feature])  # Get count of feature values
        total = len(x)
        split_info = 0.0
        for val in count.values():
            prob = val / total  # Probability of each feature value
            split_info -= prob * np.log2(prob)  # Sum the split info

        return split_info

    def __gain_ratio(self, x, y, feature):
        # Calculate the gain ratio (information gain / split info)
        info_gain = self.__information_gain(x, y, feature)  # Information gain of feature
        split_info = self.__split_information(x, feature)  # Split information of feature

        return info_gain / split_info if split_info != 0 else 0  # Avoid division by zero

    def __gini_index(self, y):
        # Calculate the Gini index for the target labels (y)
        count = Counter(y)
        total = len(y)

        gini = 1.0

        for label, cnt in count.items():
            prob = cnt / total  # Probability of each label
            gini -= prob ** 2  # Sum up Gini values

        return gini

    def __best_split_continuous(self, x, y, feature):
        unique_values = sorted(set(x[:, feature]))
        best_gain = -1
        best_threshold = None

        for i in range(1, len(unique_values)):
            threshold = (unique_values[i - 1] + unique_values[i]) / 2
            left_mask = x[:, feature] <= threshold
            right_mask = x[:, feature] > threshold

            if np.any(left_mask) and np.any(right_mask):
                left_y = y[left_mask]
                right_y = y[right_mask]
                gain = self.__entropy(y) - (
                    len(left_y)/len(y) * self.__entropy(left_y)
                    + len(right_y)/len(y) * self.__entropy(right_y)
                )

                if gain > best_gain:
                    best_gain = gain
                    best_threshold = threshold

        return best_threshold, best_gain

    def __best_split_categorical(self, x, y, features):
        best_feature = None
        best_gain_ratio = -1
        for feature in features:
            gain_ratio = self.__gain_ratio(x, y, feature)
            if gain_ratio > best_gain_ratio:
                best_gain_ratio = gain_ratio
                best_feature = feature

        return best_feature, best_gain_ratio

    def __decision_tree_helper(self, x, y, features, depth):
        if len(set(y)) == 1 or len(features) == 0 or (self.__max_depth is not None and depth >= self.__max_depth):
            majority_class = max(set(y), key=list(y).count)
            return {
                'feature': None,
                'is_leaf': True,
                'prediction': majority_class,
                'value': self.__full_class_counts(y),
                'samples': len(y),
                'gain_ratio': 0.0,
                'entropy': self.__entropy(y),
                'subtree': {}
            }

        best_feature = None
        gain_ratio = -1
        threshold = None

        for feature in features:
            if self.__feature_types[feature] == 'continuous':
                t, g = self.__best_split_continuous(x, y, feature)
                if g > gain_ratio:
                    best_feature, gain_ratio, threshold = feature, g, t
            else:
                f, g = self.__best_split_categorical(x, y, features)
                if g > gain_ratio:
                    best_feature, gain_ratio = f, g
                    threshold = None

        if best_feature is None:
            return max(set(y), key=list(y).count)

        tree = {
            'is_leaf': False,
            'feature': best_feature,
            'Depth': depth,
            'threshold': threshold,
            'value': self.__full_class_counts(y),
            'gain_ratio': gain_ratio,
            'entropy': self.__entropy(y),
            'subtree': {}
        }

        if threshold is not None:
            left_mask = x[:, best_feature] <= threshold
            right_mask = x[:, best_feature] > threshold
            tree['subtree']['<='] = self.__decision_tree_helper(x[left_mask], y[left_mask], features, depth + 1)
            tree['subtree']['>'] = self.__decision_tree_helper(x[right_mask], y[right_mask], features, depth + 1)
        else:
            for value in set(x[:, best_feature]):
                mask = x[:, best_feature] == value
                tree['subtree'][value] = self.__decision_tree_helper(x[mask], y[mask],
                                                                    [f for f in features if f != best_feature],
                                                                    depth + 1)

        return tree

    def __decision_tree(self, x, y, features, depth=0):
        # Start building the decision tree
        self.__tree = self.__decision_tree_helper(x, y, features, depth)

    def fit(self, x, y, feature_names=None, class_names=None):
        # Fit the decision tree to the data
        features = list(range(x.shape[1]))  # List of all feature indices
        self.__feature_names = feature_names  # Store feature names for later use
        self.__feature_types = ['continuous' if self.is_continuous(x[:, i]) else 'categorical' for i in range(x.shape[1])]
        self.__class_names = class_names if class_names is not None else list(set(y))
        self.__class_colors = self.__assign_class_colors(len(self.__class_names))
        self.__decision_tree(x, y, features)  # Start building the tree

    def __predict_helper(self, tree, x):
        if tree['is_leaf']:
            return tree['prediction']
        else:
            if self.__feature_types[tree['feature']] == 'continuous':
                if x[tree['feature']] <= tree['threshold']:
                    return self.__predict_helper(tree['subtree']['<='], x)
                else:
                    return self.__predict_helper(tree['subtree']['>'], x)
            else:
                return self.__predict_helper(tree['subtree'][x[tree['feature']]], x)

        return self.__predict_helper(tree['subtree'][x[tree['feature']]], x)

    def predict(self, x):
        # Predict the class labels for a set of samples (x)
        if self.__tree is None:
            raise Exception("The model has not been fitted yet.")

        predictions = [self.__predict_helper(self.__tree, sample) for sample in x]

        return np.array(predictions)  # Return predictions as a numpy array

    def score(self, x, y):
        # Calculate the accuracy of the model
        if self.__tree is None:
            raise Exception("The model has not been fitted yet.")

        predictions = self.predict(x)
        accuracy = np.mean(predictions == y)
        return accuracy

    def export_tree_to_pdf(self, filename="decision_tree"):
        if self.__tree is None:
            raise Exception("Model has not been trained yet.")

        dot = Digraph()
        self.__add_nodes(dot, self.__tree)
        dot.render(filename, format='pdf', cleanup=True)
        print(f"PDF saved as {filename}.pdf")

    def __add_nodes(self, dot, node, parent=None, edge_label=""):
        if node.get("is_leaf"):
            leaf_id = f"leaf_{id(node)}"
            class_counts = node['value']
            samples = node['samples']
            predicted_class_idx = node['prediction']
            predicted_class = self.__class_names[predicted_class_idx] if self.__class_names is not None else predicted_class_idx

            label = (
                f"samples = {samples}\n"
                f"gain ratio = {node['gain_ratio']:.3f}\n"
                f"value = {class_counts}\n"
                f"class = {predicted_class}"
            )

            color = self.__class_colors[predicted_class_idx]
            dot.node(leaf_id, label=label, shape="box", style="rounded,filled", fillcolor=color)
            if parent:
                dot.edge(parent, leaf_id, label=edge_label)
            return

        node_id = f"node_{id(node)}"
        feature_name = self.__feature_names[node['feature']] if self.__feature_names else f"Feature {node['feature']}"
        class_counts = node['value']
        samples = samples = sum(class_counts)
        predicted_class_idx = class_counts.index(max(class_counts))
        predicted_class = predicted_class_idx  # Default to index if class names are not provided

        if self.__class_names is not None:
            predicted_class = self.__class_names[predicted_class_idx]

        if node['threshold'] is not None:
            rule = f"{feature_name} <= {node['threshold']:.2f}"
        else:
            rule = f"{feature_name} = ?"

        # Build node label
        label = f"{rule}\n"
        label += f"gain ratio = {node['gain_ratio']:.3f}\n"
        label += f"samples = {samples}\n"
        label += f"value = {class_counts}\n"
        label += f"class = {predicted_class}"

        color = self.__class_colors[predicted_class_idx]  # use class index here
        dot.node(node_id, label=label, shape="box", style="rounded,filled", fillcolor=color)

        if parent:
            dot.edge(parent, node_id, label=edge_label)

        for val, subtree in node['subtree'].items():
            if node['threshold'] is not None:
                # Continuous feature — use True/False for <= and >
                edge_label = "True" if val == "<=" else "False"
            else:
                # Discrete feature — keep the actual value
                edge_label = str(val)

            self.__add_nodes(dot, subtree, parent=node_id, edge_label=edge_label)
