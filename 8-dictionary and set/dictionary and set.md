# dictionary and set

In Python, both dictionaries and sets are built-in data structures that store collections of items. However, they serve different purposes and have distinct characteristics. Here's a comparison between the two:

## Dictionary

A dictionary is an unordered collection of key-value pairs. It's defined using curly braces `{}` with key-value pairs separated by a colon `:`.

Dictionaries are mutable, meaning you can change, add, or remove key-value pairs. Suitable for scenarios where you need to associate unique keys with values, like looking up a word in a dictionary.

**Syntax**: 
```python
my_dict = {'key1': 'value1', 'key2': 'value2'}
```
**Example**:
```python
# Creating a dictionary
student_ages = {'Alice': 24, 'Bob': 22, 'Charlie': 23}

# Accessing a value
print(student_ages['Alice'])  # Output: 24

# Adding a new key-value pair
student_ages['David'] = 25

# Removing a key-value pair
del student_ages['Bob']

# Iterating over keys and values
for name, age in student_ages.items():
    print(f"{name} is {age} years old")
```


## Sets

A set is an unordered collection of unique items. It's defined using curly braces `{}` or the `set()` function.

Sets are mutable, allowing addition and removal of elements. Useful for mathematical set operations like union, intersection, and difference, and for eliminating duplicate entries from a collection.
 
**Syntax**: 
```python
  my_set = {'item1', 'item2', 'item3'}
  another_set = set(['item1', 'item2', 'item3'])
```

**Example**:

```python
# Creating a set
fruits = {'apple', 'banana', 'cherry'}

# Adding an item
fruits.add('date')

# Removing an item
fruits.remove('banana')

# Checking membership
if 'apple' in fruits:
    print("Apple is in the set")

# Iterating over items
for fruit in fruits:
    print(fruit)
```


