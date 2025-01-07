# Code Implementation
def is_palindrome(word):
    # Remove spaces and convert to lowercase
    sanitized_word = ''.join(word.split()).lower()
    
    # Check if the word is the same forwards and backwards
    return sanitized_word == sanitized_word[::-1]

# Test examples
words = ["civic", "radar", "level", "rotor", "kayak", "race car", "hello"]

# Loop through each word and test if it's a palindrome
for word in words:
    if is_palindrome(word):
        print(f"'{word}' is a palindrome.")
    else:
        print(f"'{word}' is not a palindrome.")
