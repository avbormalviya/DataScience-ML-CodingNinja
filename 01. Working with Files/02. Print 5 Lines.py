
# Problem statement

""" Given file "Sample.txt"
Open the file
Read the first 5 lines from file and print them (in separate lines).

Output Format :
Line 1
Line 2
Line 3
Line 4
Line 5 """


# Solution


from itertools import islice  # Import islice to efficiently read limited lines


# Open the file in read mode
with open("dataset.txt", "r") as fileObj:
    # Use islice to read only the first 5 lines (memory-efficient)
    for line in islice(fileObj, 5):
        print(line.strip())  # `strip()` removes extra newline characters
