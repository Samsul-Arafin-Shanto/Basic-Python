# Float to int
float_num = 3.7
print(int(float_num))  # Output: 3

# String to int
str_num = "42"
print(int(str_num))  # Output: 42

# String (float) to int
str_num = "3.7"
print(int(float(str_num)))  # Output: 3

# Boolean to int
bool_val = True
print(int(bool_val))  # Output: 1

# List to int
my_list = [42]
print(int(my_list[0]))  # Output: 42

# Tuple to int
my_tuple = (3.7,)
print(int(my_tuple[0]))  # Output: 3

# None to int
none_val = None
print(int(none_val or 0))  # Output: 0

# Complex to int
complex_num = 3 + 4j
print(int(complex_num.real))  # Output: 3

# Binary to int
binary_num = "1010"  # Binary for 10
int_num = int(binary_num, 2)
print(f"Binary {binary_num} to int: {int_num}")  # Output: 10

# Octal to int
octal_num = "12"  # Octal for 10
int_num = int(octal_num, 8)
print(f"Octal {octal_num} to int: {int_num}")  # Output: 10

# Hexadecimal to int
hex_num = "A"  # Hexadecimal for 10
int_num = int(hex_num, 16)
print(f"Hexadecimal {hex_num} to int: {int_num}")  # Output: 10