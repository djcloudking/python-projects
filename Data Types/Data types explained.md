# Python data types explained

Data types specify the kind of value a variable can hold.


## Basic Data Types

### Integers (int)
        
Think of counting shoes. You have whole shoes: 1, 2, 3, etc.

Example: 10 shoes, -3 debts


### Floating-Point Numbers (float)

Imagine measuring ingredients for a recipe. You need 2.5 cups of flour.

Example: 3.14 (like pi), -0.001 (a tiny negative amount)


### Complex Numbers (complex)

This is like having a two-part value, such as temperature (real) and humidity (imaginary).
        
Example: 3 + 4j (where j represents the imaginary part)


### Booleans (bool)

Think of a light switch. It can be either on (True) or off (False).
        
Example: True (the light is on), False (the light is off)


### Strings (str)
        
These are sequences of characters, like words or sentences you read in a book.
        
    1. String Data Type in Python:

        In Python, a string is a sequence of characters, enclosed within single (' '), double (" "), or triple (''' ''' or """ """) quotes.

        You can access individual characters in a string using indexing, e.g., my_string[0] will give you the first character.

        Strings support various built-in methods, such as len(), upper(), lower(), strip(), replace(), and more, for manipulation.

    2. String Manipulation and Formatting:

        Concatenation: You can combine strings using the + operator.

        Substrings: Use slicing to extract portions of a string, e.g., my_string[2:5] will extract characters from the 2nd to the 4th position.

        String interpolation: Python supports various ways to format strings, including f-strings (f"...{variable}..."), %-formatting ("%s %d" % ("string", 42)), and str.format().

        Escape sequences: Special characters like newline (\n), tab (\t), and others are represented using escape sequences.

        String methods: Python provides many built-in methods for string manipulation, such as split(), join(), and startswith().


## Collection Data Types


### Lists (list)
        
Like a shopping list where you can add or remove items.

Example: ['milk', 'eggs', 'bread']


### Tuples (tuple)
        
Imagine a coordinate (x, y) that doesn't change, like GPS coordinates.

Example: (34.0522, -118.2437) (coordinates for Los Angeles)


### Dictionaries (dict)
        
Think of a phone book where you look up a name to get a phone number.
        
Example: {'Alice': '123-4567', 'Bob': '987-6543'}


### Sets (set)
        
Like a collection of unique stickers. No duplicates allowed.

Example: {'red', 'blue', 'green'}


### Frozen Sets (frozenset)
        
This is like a set but in a frame. You can't change it once it's made.
        
Example: frozenset({'red', 'blue', 'green'})


## Specialized Data Types


### Bytes (bytes)
        
Think of raw binary data, like a digital fingerprint.
        
Example: b'hello' (raw byte data for the word "hello")


### Byte Arrays (bytearray)
        
Like bytes, but you can change them, similar to editing a text file.
        
Example: bytearray(b'hello') (editable raw byte data)


### Memory Views (memoryview)
        
Think of looking at a slice of data without copying it, like peeking into a book without removing the page.
        
Example: memoryview(b'hello') (viewing part of the raw byte data)