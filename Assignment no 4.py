#3 Task no 1

filename = "sample.txt"

try:
    with open(filename, "r") as file:
        print("Reading file content:\n")
        for line_number, line in enumerate(file, start=1):
            print(f"Line {line_number}: {line.strip()}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

Output:
Reading file content:

Line 1: This is sample text file.
Line 2: It contains multiple lines.

# AND

filename = "sample.txt"

try:
    with open(filename, "r") as file:
        print("Reading file content:\n")
        for line_number, line in enumerate(file, start=1):
            print(f"Line {line_number}: {line.strip()}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

Output:
Error: The file 'sample.txt' was not found.

#3 Task no 2

file1 = open('output.txt', 'a')
appending_file1=file1.write('\nLearning file handling in Python.')
file1.close()

file1 = open('output.txt', 'r')
reading_file = file1.read()
print(reading_file)
file1.close()

Output:
Hello, Pyhton!
Learning file handling in Python.
