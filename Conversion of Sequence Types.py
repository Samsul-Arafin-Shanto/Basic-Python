# Define the objects
a = [1, 2, 3, 4, 5]  # List Object
b = (1, 2, 3, 4, 5)  # Tuple Object
c = "Hello"          # String Object

# Convert string to list using list()
obj = list(c)  # Separates each character in the string and builds a list
print("String to list:", obj)  # Output: ['H', 'e', 'l', 'l', 'o']

# Convert tuple to list using list()
obj = list(b)  # Replaces parentheses of tuple with square brackets
print("Tuple to list:", obj)  # Output: [1, 2, 3, 4, 5]

# Convert string to tuple using tuple()
obj = tuple(c)  # Separates each character in the string and builds a tuple
print("String to tuple:", obj)  # Output: ('H', 'e', 'l', 'l', 'o')

# Convert list to tuple using tuple()
obj = tuple(a)  # Replaces square brackets of list with parentheses
print("List to tuple:", obj)  # Output: (1, 2, 3, 4, 5)

# Convert list to string using str()
obj = str(a)  # Puts the list inside quote symbols as a string
print("List to string:", obj)  # Output: '[1, 2, 3, 4, 5]'

# Convert tuple to string using str()
obj = str(b)  # Puts the tuple inside quote symbols as a string
print("Tuple to string:", obj)  # Output: '(1, 2, 3, 4, 5)'