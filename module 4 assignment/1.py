# Write a Python program to read an entire text file.

file = open("3.py", "r")

# Read the entire contents of the file
content = file.read()

file.close()

print(content)