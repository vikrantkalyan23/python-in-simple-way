list1 = []  # empty list

print(list1)
print(type(list1))

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(list1)

list2 = [1, 2, "Hello", True, 10.5]
print(list2)

# Indexing (same as string)

print(list1[1])
print(list1[4:])
print(list1[:5])
print(list1[-2:])
print(list1[:-3])

# List Length
print(len(list1))

# Sorting

list3 = [2, 5, 1, 3, 7, 11, 10, 24, 50, 22]
list3.sort() # for reverse sorting .sort(reverse=True)
print(list3)
