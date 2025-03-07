# Integer to string
int_num = 10
str_num = str(int_num)
print(f"Integer {int_num} to string: {str_num}")  # Output: "10"

# Float to string
float_num = 3.14
str_num = str(float_num)
print(f"Float {float_num} to string: {str_num}")  # Output: "3.14"

# Boolean to string
bool_val = True
str_num = str(bool_val)
print(f"Boolean {bool_val} to string: {str_num}")  # Output: "True"

# List to string
my_list = [1, 2, 3]
str_num = str(my_list)
print(f"List {my_list} to string: {str_num}")  # Output: "[1, 2, 3]"

# Tuple to string
my_tuple = (4, 5, 6)
str_num = str(my_tuple)
print(f"Tuple {my_tuple} to string: {str_num}")  # Output: "(4, 5, 6)"

# None to string
none_val = None
str_num = str(none_val)
print(f"None {none_val} to string: {str_num}")  # Output: "None"

# Binary to string
binary_num = "1010"  # Binary for 10
int_num = int(binary_num, 2)  # First convert binary to integer
str_num = str(int_num)  # Then convert integer to string
print(f"Binary {binary_num} to string: {str_num}")  # Output: "10"

# Octal to string
octal_num = "12"  # Octal for 10
int_num = int(octal_num, 8)  # First convert octal to integer
str_num = str(int_num)  # Then convert integer to string
print(f"Octal {octal_num} to string: {str_num}")  # Output: "10"

# Hexadecimal to string
hex_num = "A"  # Hexadecimal for 10
int_num = int(hex_num, 16)  # First convert hexadecimal to integer
str_num = str(int_num)  # Then convert integer to string
print(f"Hexadecimal {hex_num} to string: {str_num}")  # Output: "10"

# Binary with prefix to string
binary_num_with_prefix = "0b1010"  # Binary for 10 with prefix
int_num = int(binary_num_with_prefix, 2)  # First convert binary to integer
str_num = str(int_num)  # Then convert integer to string
print(f"Binary {binary_num_with_prefix} to string: {str_num}")  # Output: "10"

# Octal with prefix to string
octal_num_with_prefix = "0o12"  # Octal for 10 with prefix
int_num = int(octal_num_with_prefix, 8)  # First convert octal to integer
str_num = str(int_num)  # Then convert integer to string
print(f"Octal {octal_num_with_prefix} to string: {str_num}")  # Output: "10"

# Hexadecimal with prefix to string
hex_num_with_prefix = "0xA"  # Hexadecimal for 10 with prefix
int_num = int(hex_num_with_prefix, 16)  # First convert hexadecimal to integer
str_num = str(int_num)  # Then convert integer to string
print(f"Hexadecimal {hex_num_with_prefix} to string: {str_num}")  # Output: "10"