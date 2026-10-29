str1 = "This is a String Example in Python"

print("String : ", str1)
print("String Length : ", len(str1))
print("Data Type : ", type(str1))

str2 = "String is a collection of characters"

# String Concatenation
print(str1 + str2)
print(str1 + " " + str2)
print(str1 + "\n" + str2)
print(f"{str1} {str2}")

# Multiline String
str3 ="""
This is a 
multiline
string
"""
print(str3)


# Indexing of String

print("First Element of string : ", str1[0])
print("Second Element of string : ", str1[1])

#   0   1   2   3   4   5   6       ## Indexing
#   V   I   K   R   A   N   T
#   -7  -6  -5  -4  -3  -2  -1      ## Reverse/Negative Indexing


# Slicing
# result = stringVariable[startIndex:endIndex]

name = "Vikrant Kumar"
print(name[3:])     # from 3rd index to end of string
print(name[:10])    # from 0th index to 9th (10th not included)
print(name[2:5])

print(name[-7:])
print(name[:-3])
print(name[-7:-2])

# Library functions 
print("Length of string :",len(name))
print(name.isnumeric())
print(name.startswith("V"))
print(name.find("a"))
print(name.endswith("r"))
print(name.split(" "))

a = "Hello, World!"
print(a.replace("H", "J"))

a = " Hello, World! "
print(a.strip())    # remove space from beginning and end  
print(a.upper())
print(a.lower())

# stringName[startIndex:endIndex:skipCharacters]

print(a[::-1]) # Reverse String

# String Methods (Cleaning, Formatting, Validation, Transformation)

# strip(), lstrip(), rstrip()

# replace()

# upper(), lower(), title()

# split(), join()

# isNumeric()

# startsWith()

# endWith()

# count()

# find()

# index()

email = "sample@vikrant.com"
domain = email[email.find("@")+1:]
print(domain)

priceTxt ="Price:  ₹240/-"
cleanedPrice=priceTxt.replace("Price:","").replace("₹","").replace("/-","").strip()
print(cleanedPrice)