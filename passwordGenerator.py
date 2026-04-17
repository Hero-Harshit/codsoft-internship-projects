import secrets
import time

# Data sets
small_letters = [chr(i) for i in range(97, 123)]
capital_letters = [chr(i) for i in range(65, 91)]
numbers = [str(i) for i in range(10)]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']

print("Hello! Welcome to the password generator.")
time.sleep(1)
print("This program will generate a random password based on your choices.")
time.sleep(1)

# Validate length input
try:
    length = int(input("Enter password length: ").strip())
    if length <= 0:
        print("Length must be greater than 0.")
        exit()
except ValueError:
    print("Please enter a valid number.")
    exit()

# User choices
include_capital = input("Include capital letters? (y/n): ").strip().lower().startswith('y')
include_numbers = input("Include numbers? (y/n): ").strip().lower().startswith('y')
include_symbols = input("Include symbols? (y/n): ").strip().lower().startswith('y')

print("\nGenerating your password...")
time.sleep(1)

# Build character pool
master_list = []
master_list.extend(small_letters)

selected_groups = [small_letters]

if include_capital:
    master_list.extend(capital_letters)
    selected_groups.append(capital_letters)

if include_numbers:
    master_list.extend(numbers)
    selected_groups.append(numbers)

if include_symbols:
    master_list.extend(symbols)
    selected_groups.append(symbols)

# Ensure at least one character from each selected group
password_chars = [secrets.choice(group) for group in selected_groups]

# Fill remaining length
while len(password_chars) < length:
    password_chars.append(secrets.choice(master_list))

# Shuffle for randomness
secrets.SystemRandom().shuffle(password_chars)

generated_password = ''.join(password_chars)

print("Your automated generated & secured password is:", generated_password)
print("Don't Share your passwords with anyone.")

# End