# Command Line Arguments, Environment Variables, Operators and Conditional Handling


- **Command Line Arguments:** Use the `sys.argv` list to access arguments passed to a Python script.

- **Environment Variables:** Use the `os` module to get and set environment variables.

- **Operators:** Use various operators to perform arithmetic, comparison, logical, and bitwise operations.

- **Conditional Handling:** Use `if`, `elif`, and `else` statements to execute code based on conditions.


## Command Line Arguments

In Python, command line arguments are inputs provided to a script when it is executed. These arguments are accessible via the `sys.argv` list from the `sys` module.

**Example:**
```python
import sys

# sys.argv[0] is the name of the script
# sys.argv[1:] are the command line arguments
print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])
```

If you run this script with arguments:
```bash
python script.py arg1 arg2 arg3
```
It will output:
```
Script name: script.py
Arguments: ['arg1', 'arg2', 'arg3']
```

## Environment Variables

Environment variables are used to configure the behavior of the system and applications. In Python, you can access and set environment variables using the `os` module.

**Example:**
```python
import os

# Get the value of an environment variable
path = os.getenv('PATH')
print("PATH:", path)

# Set an environment variable
os.environ['MY_VARIABLE'] = 'my_value'
print("MY_VARIABLE:", os.environ['MY_VARIABLE'])
```

## Operators

Operators in Python are used to perform operations on variables and values. They include arithmetic, comparison, logical, and bitwise operators.

**Examples:**

**Arithmetic Operators:**
```python
a = 5
b = 2
print(a + b)  # Addition: 7
print(a - b)  # Subtraction: 3
print(a * b)  # Multiplication: 10
print(a / b)  # Division: 2.5
print(a % b)  # Modulus: 1
print(a ** b) # Exponentiation: 25
```

**Comparison Operators:**
```python
print(a == b)  # Equal: False
print(a != b)  # Not equal: True
print(a > b)   # Greater than: True
print(a < b)   # Less than: False
print(a >= b)  # Greater than or equal to: True
print(a <= b)  # Less than or equal to: False
```

**Logical Operators:**
```python
print(a > 1 and b < 3)  # Logical AND: True
print(a > 1 or b > 3)   # Logical OR: True
print(not(a > 1))       # Logical NOT: False
```

**Bitwise Operators:**
```python
print(a & b)  # Bitwise AND: 0
print(a | b)  # Bitwise OR: 7
print(a ^ b)  # Bitwise XOR: 7
print(~a)     # Bitwise NOT: -6
```

## Conditional Handling

Conditional handling allows the execution of different code blocks based on certain conditions. This is achieved using `if`, `elif`, and `else` statements.

**Example:**
```python
x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
```

**Ternary Conditional Operator:**
```python
a = 5
b = 10
max_value = a if a > b else b
print("Max value:", max_value)  # Max value: 10
```