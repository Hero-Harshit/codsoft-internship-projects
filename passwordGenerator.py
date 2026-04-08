# Importing necessary libraries

import random
import time

# Main Data Sets

small_letters = [chr(i) for i in range(97, 123)]
capital_letters = [chr(i) for i in range(65, 91)]
numbers = [str(i) for i in range(10)]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']

# Beginning of the program

print("Hello! Welcome to the password generator.")
time.sleep(1)
print("This program will generate a random password for you based on the criteria you choose.")
time.sleep(1)
print("You can choose to include small letters, large letters, numbers, and symbols in your password.")
time.sleep(1)
print("Let's get started !")
time.sleep(1)
print("First, let's choose the length of your password.")
time.sleep(1)
length = int(input("Input the length of the password you want to generate: "))
print("The length of your password will be: ", length)
time.sleep(1)
print("Great! Now let's choose the criteria for your password.")
include_capital_letters = input("Do you want to include capital letters ? (y/n): ").lower()
include_numbers = input("Do you want to include numbers ? (y/n): ").lower()
include_symbols = input("Do you want to include symbols ? (y/n): ").lower()
print("")
print("Generating your password...")
time.sleep(1)

master_list = []

if include_capital_letters == 'y':
    master_list.extend(capital_letters)

if include_numbers == 'y':
    master_list.extend(numbers)

if include_symbols == 'y':
    master_list.extend(symbols)

generated_password = ""

for i in range(length):
    generated_password += random.choice(master_list)

print("Your generated password is: ", generated_password)