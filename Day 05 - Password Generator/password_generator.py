import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"

# User input
num_letters = int(input("How many letters would you like in your password? "))
num_numbers = int(input("How many numbers would you like? "))
num_symbols = int(input("How many symbols would you like? "))

# Generate password list using for loops
password_list = []

# Add random letters
for _ in range(num_letters):
    password_list.append(random.choice(letters))

# Add random numbers
for _ in range(num_numbers):
    password_list.append(random.choice(numbers))

# Add random symbols
for _ in range(num_symbols):
    password_list.append(random.choice(symbols))

# Shuffle the password
random.shuffle(password_list)

# Convert list to string
password = "".join(password_list)

# Print the password
print(f"Your generated password is: {password}")


# import random

# letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# numbers = "0123456789"
# symbols = "!@#$%^&*()"

# # User input
# num_letters = int(input("How many letters would you like in your password? "))
# num_numbers = int(input("How many numbers would you like? "))
# num_symbols = int(input("How many symbols would you like? "))

# # Generate password list
# password_list = []
# password_list.extend(random.choices(letters, k=num_letters))
# password_list.extend(random.choices(numbers, k=num_numbers))
# password_list.extend(random.choices(symbols, k=num_symbols))

# # Shuffle the password
# random.shuffle(password_list)

# # Convert list to string
# password = "".join(password_list)

# # Print the password
# print(f"Your generated password is: {password}")
