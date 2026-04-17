import random
import time

choices = ["R", "P", "S"]

print("Welcome to Rock, Paper, Scissors Game!")
time.sleep(1)
print("You will be playing against the computer.")
time.sleep(1)
print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
time.sleep(1)
print('Press "R" for Rock, "P" for Paper, and "S" for Scissors.')
time.sleep(1)

# Validate rounds input
try:
    rounds = int(input("How many rounds would you like to play? ").strip())
    if rounds <= 0:
        print("Rounds must be greater than 0.")
        exit()
except ValueError:
    print("Please enter a valid number.")
    exit()

print(f"\nGreat! Let's play {rounds} rounds.\n")

computer_score = 0
player_score = 0

for round_num in range(1, rounds + 1):
    while True:
        player_choice = input(f"Round {round_num} - Enter your choice (R/P/S): ").strip().upper()
        
        if player_choice in choices:
            break
        else:
            print("Invalid choice! Please enter R, P, or S.")

    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (
        (player_choice == "R" and computer_choice == "S") or
        (player_choice == "P" and computer_choice == "R") or
        (player_choice == "S" and computer_choice == "P")
    ):
        print("You won this round!")
        player_score += 1
    else:
        print("Computer won this round!")
        computer_score += 1        

    print(f"Score: Player {player_score} - Computer {computer_score}")
    
    if round_num != rounds:
        time.sleep(1)
        print("Next round...\n")

# Final result
print("\n--- Final Result ---")
if player_score > computer_score:
    print(f"Congratulations! You won {player_score} to {computer_score}! 🎉")
elif computer_score > player_score: 
    print(f"Computer wins {computer_score} to {player_score}. Better luck next time!")
else:
    print(f"It's a tie! Both scored {player_score}.")