import sys

def add(a, b):
    add = a + b
    return add

def sub(a, b):
    sub = a - b
    return sub

def mul(a, b):
    mul = a * b
    return mul

num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "add":
    output = add(num1, num2)
    print(output)