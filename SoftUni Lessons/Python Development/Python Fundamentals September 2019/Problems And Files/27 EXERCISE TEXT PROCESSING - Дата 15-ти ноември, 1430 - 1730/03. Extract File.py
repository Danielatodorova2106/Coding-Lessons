"""
Text Processing - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1740#2

SUPyF2 Text-Pr.-Ex. - 03. Extract File

Problem:
Write a program that reads the path to a file and subtracts the file name and its extension.

Examples:
Input:
C:\Internal\training-internal\Template.pptx
Output:
File name: Template
File extension: pptx

Input:
C:\Projects\Data-Structures\LinkedList.cs
Output:
File name: LinkedList
File extension: cs
"""

# This was the initial Solution:
"""
text = input()[::-1]
new_text = ""

for letter in text:
    if letter == "\\":
        break
    new_text += letter
file, extension = new_text[::-1].split(".")
print(f"File name: {file}")
print(f"File extension: {extension}")
"""

# Second Solution at Class

full_file = input().split("\\")[-1]
file_name = full_file.split(".")[0]
file_extension = full_file.split(".")[1]

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")


































