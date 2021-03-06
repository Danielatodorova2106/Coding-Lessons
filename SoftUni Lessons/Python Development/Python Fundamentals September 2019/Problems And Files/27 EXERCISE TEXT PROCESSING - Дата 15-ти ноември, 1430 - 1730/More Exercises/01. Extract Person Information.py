"""
Text Processing - More Exercises
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1741#0

SUPyF2 Text-Pr.-More-Ex. - 01. Extract Person Information

Problem:
Write a program that reads N lines of strings and extracts the name and age of a given person.
The name of the person will be between '@' and '|'. The person’s age will be between '#' and '*'.
Example: "Hello my name is @Peter| and I am #20* years old."
For each found name and age print a line in the following format "{name} is {age} years old."

Example:
Input:
2
Here is a name @George| and an age #18*
Another name @Billy| #35* is his age

Output:
George is 18 years old.
Billy is 35 years old.

Input:
3
random name @lilly| random digits #5* age
@Marry| with age #19*
here Comes @Garry| he is #48* years old

Output:
lilly is 5 years old.
Marry is 19 years old.
Garry is 48 years old.
"""

# There are two ways I can solve this problem. One of them will be with the use of Regex
# But unfortunately I can't check it if it's correct or not as the Time limit in Judge
# doesn't allow as to. But Still there is the solution:
"""
import re

for i in range(int(input())):
    text = input()
    name = re.findall(r"@\w+\|", text)[0].strip("@").strip("|")
    age = re.findall(r"#\d+\*", text)[0].strip("#").strip("*")
    print(f"{name} is {age} years old.")
"""

# And the Second Solution, which will be accepted, one way ot another is this:
for text in range(int(input())):
    line = [letter for letter in input()]
    name = ''.join(line[(line.index("@") + 1):line.index("|")])
    age = ''.join(line[(line.index("#") + 1):line.index("*")])
    print(f"{name} is {age} years old.")

