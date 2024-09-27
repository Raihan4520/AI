# python loop

# While loop is general purpose loop in python

i = 1

while i <= 10:
    print(i)
    # Can use both but cannot use i++ in python
    # i=i+1
    i += 1

print("Loop through a list")

lst = [5, 1, 2, 8, 9, 5, "abc", 2.5]

i = 0

while i < len(lst):
    print(lst[i])
    i += 1

print("For Loop")
# For loop is a special purpose loop
# For loop can be used to iterate through a list

# for variableName in listName

for item in lst:  # Like for each loop
    print(item)

print("Print a range of number")
numberList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in numberList:
    print(n)

# range(start, end-1, step size) (by default start = 0 and step size = 1)
# Returns a list of specific range
numberList = range(50, 101, 5)  # prints 50 to 100

for n in numberList:
    print(n)


# b has a default value of 1
# always set default parameter from last (Cannot be (a=5,b))


def myFunction(a, b=1):  # No need to write any return type in python
    print("This is My Function")
    c = a+b
    return c


# if value of b is passed then it will override default value 1
result = myFunction(5)

print(result)

# List has a numeric index
cgpaList = [3.5, 2.5, 2.8, 3.2, 2.9]
#            0    1    2    3    4

# Dictionary
# Dictionary has a string index
# We save data in a dictionary as key:value pair.

cgpaDictionary = {"James": 3.5, "Julia": 2.5,
                  "Pence": 3.8, "Rafi": 3.2, "Ashik": 2.9}

# print(cgpaDictionary["James"])
# print(cgpaDictionary["Julia"])

print(cgpaDictionary)

cgpaDictionary["Pence"] = 3.5  # Updating an exhisting value
cgpaDictionary["newStudent"] = 0.0  # Adding a new key value pair

# Use del or pop to delete a specific key value pair
cgpaDictionary.pop("James")

# Use clear to delete a dictionary
# cgpaDictionary.clear()

print(cgpaDictionary)

# For loop for dictionary
print("Print the keys of a dictionary")
for item in cgpaDictionary:  # It will only print key
    print(item)


print("Print values of a dictionary")
for item in cgpaDictionary.values():
    print(item)

print("Print key and value both")
for key, value in cgpaDictionary.items():
    # if value == 3.2:
    #     print(key)
    # if value >= 3.0:
    #     print(key)
    print(key, "--->", value)


# Always write all functions on top


def myFunction2(a, b):
    add = a+b
    sub = a-b
    return (add, sub)  # Returning a tuple


result = myFunction2(7, 2)
print(result[0], result[1])

# Tuple
# Once you have created a tuple you cannot change any item
# To change a tuple convert it to a list then change it and again convert it back to a tuple
# Loop through a tuple like a list

tup = (5, 1, "ABC", 2.5)  # Packing a tuple

# Print by index
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])

a, b, c, d = tup  # Unpacking a tuple
print("abcd --->", a, b, c, d)


print("\nSet operation\n")
# Set
# Not key value pair like dictionary. It has only value
# For set, you cannot use index
# No value can be updated like tuple but value can be added or deleted
# By default sorts value in ascending order
mySet = {2, 1, 6, 'Hello', 2.5}

mySet.add("NewValue")
mySet.add(3)
mySet.remove(2.5)

for item in mySet:
    print(item)

if 16 in mySet:
    print("Value exist")
else:
    print("Value doesn't exist")
