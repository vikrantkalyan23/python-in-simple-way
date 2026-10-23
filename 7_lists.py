# Lists are used to store multiple items in a single variable.
# List items are ordered, changeable, and allow duplicate values.


list1 = []  # empty list

print(list1)
print(type(list1))

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(list1)

list2 = [1, 2, "Hello", True, 10.5]
print(list2)

# Access Items
# Indexing (same as string)

print(list1[1])
print(list1[4:])
print(list1[:5])
print(list1[-2:])
print(list1[:-3])

# Check if Item Exists

if "Hello" in list2:
    print("Hello is exists in list2")

# List Length
print(len(list1))

# Sorting

list3 = [2, 5, 1, 3, 7, 11, 10, 24, 50, 22]
list3.sort()  # for reverse sorting .sort(reverse=True)
print(list3)

# Check if Item Exists

list3[2] = 15  # Change Item Value
print(list3)

list3[1:3] = [19, 20]  # Change a Range of Item Values
list3[1:3] = [37]  # Change the second and third value by replacing it with one value
print(list3)

# Add Item

list3.append(21)  # Append
print(list3)

list3.insert(2, 33)  # Insert at second index
print(list3)

# Extend List -> To append elements from another list to the current list, use the extend() method.
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

thisList = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thisList.extend(tropical)
print(thisList)

thisList = ["apple", "banana", "cherry"]
thisTuple = ("kiwi", "orange")
thisList.extend(thisTuple)
print(thisList)

# Remove List Items -> The remove() method removes the specified item

list3.remove(33)  # Remove by value
print(list3)

list3.pop(2)  # Remove Specified Index

# The del keyword also removes the specified index

thisList = ["apple", "banana", "cherry"]
del thisList[0]
print(thisList)

# The del keyword can also delete the list completely.
thisList = ["apple", "banana", "cherry"]
del thisList

# Clear the List -> The clear() method empties the list. The list still remains, but it has no content.
tropical.clear()
print(tropical)

# Loop Through a List

thisList = ["apple 1", "banana 2", "cherry 3"]
for fruit in thisList:
    print(fruit)

# Loop Through the Index Numbers -> Use the range() and len() functions to create a suitable iterable.

thisList = ["apple 2", "banana 2", "cherry 2"]
for i in range(len(thisList)):
    print(thisList[i])

# Using a While Loop

i = 0
while i < len(thisList):
    print(thisList[i])
    i = i + 1

# Looping Using List Comprehension

[print(x) for x in thisList]
