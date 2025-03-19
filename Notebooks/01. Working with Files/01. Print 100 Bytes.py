
# Problem statement

""" Given file "Sample.txt"
Open the file
Read the first 100 bytes of file and print them. """


# Solution


with open("dataset.txt", "r") as fileObj:  # "r" mode (default) for reading
    print(fileObj.read(100))  # Read first 100 characters
