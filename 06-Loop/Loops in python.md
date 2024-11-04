# Loop statement

Use to perform a repetiive action on a block of code. 

## for loop

Use to execute a block of code for a specific number of times.

Syntax: for i in range(5)

**i** is a variable
**in** keyword
**range(x)** is like sequence, a list of number from 0 to x. Sequence can be range, list or tuple. 


## while loop

Use to execute a block of code for unknown number of times (dynamically).

Syntax: while condition:

# Loop manipulation


## break

Use to terminate a loop when a particular condition is met.

Example:

numbers = [1, 2, 3, 4]
for num in numbers:
    if number == 3:
        break
    print(number)

Output:
1
2

## continue

Use to skip the iteration in a loop when the condition is met.

Example:

numbers = [1, 2, 3, 4]
for num in numbers:
    if number == 3:
        contiue
    print(number)

Output:
1
2
3
4