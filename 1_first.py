"""
Python is high level, interpreted, general purpose programming language.

Python is case sensitive, means name and Name treated as different.

"""

# Single Line Comment

""" 
----Multi-line Comment---

Used
to 
comment
Multi-line
lines
"""

"""
Also 
Multi-line 
comment
"""


# print() is used to print any message or variable

print("Hello this is my first program")

name = "Vikrant"
age = 30
print(name)

# String and variable concatenation with comma
print("Name :", name, "and Age : ", age)

# f-string
print(f"Name : {name} and Age {age}")

# Format method
print("My name is {} and my age is {}".format(name, age))

# User Input
name = input("Enter name :")
print(f"My name is {name}")

age = int(input("Enter age : "))
print(f"My age is {age}")
