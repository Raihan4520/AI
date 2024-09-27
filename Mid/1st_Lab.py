print("Hello World")

# Single line comment

'''
Multiple
Line
Comment
'''

# OR

"""
Multiple
Line
Comment
"""

# C++ End of a statement represented by ;
# Python End of a statement represented by newline or ;

a = 5;
b = 2.5
c = "This is a string"
d = 'g';

s = a + b

# Not prefered to write like this (Use one line for each)
print(a); print(b); print(c); print(d)

print(type(a))
print(type(b))
print(type(c));
print(type(d));
print(type(s))

a = "Now it is a string"
print(a)
print("New data type of a is :", type(a))


# Can use both but first one is more preferable
a = int(input("Please enter a number: "))

print("Please enter another number:", end=' ')
b = float(input())

c = a + b
print("Output:", c)

if a < 10:
    print("a < 10")
    print("This is if block")
elif a >= 10 and a <= 20:
    print("a >= 10 and a <= 20")
    print("This is else if block")
else:
    print("a > 20")
    print("This is else block")

print("This is outside the if else block")


arr = [4, 9, 1, 2.5, 'abc']

print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])

print(arr)

print("Value chnaged")
arr[1] = 20
print(arr[1])
print(arr)

arr.append(100)
arr.append(200)
arr[6] = 30
print(arr)

arr.insert(1, 'xyz')
arr[1] = 'xyz'
print(arr)

arr.remove(2.5)
print(arr)

print(len(arr))
