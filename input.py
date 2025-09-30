# Hunt-2059
# This script reads from 'input.txt', processes the data, and writes to 'output.txt'.
import os

print("Looking in:", os.getcwd())  # shows where Python is searching

try:
    test = input("Enter the desired file names to check if file exists: ")
    with open(test, "r") as f:
        print(f"File {test} exists.")
except FileNotFoundError:
    print(f"File {test} does not exist. Please check the file name and try again.")
    print("\n")

try:
    with open("input.txt", "r") as infile:
        data = infile.readlines()
        print(data)
    processed_data = [line.upper() for line in data]
    print(processed_data)
    
    with open("output.txt", "w") as outfile:
        outfile.writelines(processed_data)
        print("Write operation successful.")
except FileNotFoundError:
    print("File not found. Try checking file path.")
