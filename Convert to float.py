# 1. Convert Integer to Float
int_num = 10
float_num = float(int_num)
print(f"Integer {int_num} to float: {float_num}")  # Output: 10.0

# 2. Convert String (Integer) to Float
str_num = "42"
float_num = float(str_num)
print(f"String '{str_num}' to float: {float_num}")  # Output: 42.0

# 3. Convert String (Float) to Float
str_float = "3.14"
float_num = float(str_float)
print(f"String '{str_float}' to float: {float_num}")  # Output: 3.14

# 4. Convert Boolean to Float
bool_val = True
float_num = float(bool_val)
print(f"Boolean {bool_val} to float: {float_num}")  # Output: 1.0

# 5. Convert Binary to Float
binary_num = "1010"  # Binary for 10
int_num = int(binary_num, 2)  # First convert binary to integer
float_num = float(int_num)  # Then convert integer to float
print(f"Binary '{binary_num}' to float: {float_num}")  # Output: 10.0

# 6. Convert Octal to Float
octal_num = "12"  # Octal for 10
int_num = int(octal_num, 8)  # First convert octal to integer
float_num = float(int_num)  # Then convert integer to float
print(f"Octal '{octal_num}' to float: {float_num}")  # Output: 10.0

# 7. Convert Hexadecimal to Float
hex_num = "A"  # Hexadecimal for 10
int_num = int(hex_num, 16)  # First convert hexadecimal to integer
float_num = float(int_num)  # Then convert integer to float
print(f"Hexadecimal '{hex_num}' to float: {float_num}")  # Output: 10.0

# 8. Convert Binary with Prefix to Float
binary_num_with_prefix = "0b1010"  # Binary for 10 with prefix
int_num = int(binary_num_with_prefix, 2)  # First convert binary to integer
float_num = float(int_num)  # Then convert integer to float
print(f"Binary '{binary_num_with_prefix}' to float: {float_num}")  # Output: 10.0

# 9. Convert Octal with Prefix to Float
octal_num_with_prefix = "0o12"  # Octal for 10 with prefix
int_num = int(octal_num_with_prefix, 8)  # First convert octal to integer
float_num = float(int_num)  # Then convert integer to float
print(f"Octal '{octal_num_with_prefix}' to float: {float_num}")  # Output: 10.0

# 10. Convert Hexadecimal with Prefix to Float
hex_num_with_prefix = "0xA"  # Hexadecimal for 10 with prefix
int_num = int(hex_num_with_prefix, 16)  # First convert hexadecimal to integer
float_num = float(int_num)  # Then convert integer to float
print(f"Hexadecimal '{hex_num_with_prefix}' to float: {float_num}")  # Output: 10.0

# 11. Convert None to Float (with default value)
none_val = None
float_num = float(none_val or 0)  # Replace None with 0, then convert to float
print(f"None to float: {float_num}")  # Output: 0.0