import random
import time

choices = ["R", "P", "S"]

print("Welcome to Rock, Paper, Scissors Game ! ")
time.sleep(1)
print("You will be playing against the computer.")
time.sleep(1)
print("The rules are simple: Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.")
time.sleep(1)
print('Press "R" for Rock, "P" for Paper, and "S" for Scissors.')
time.sleep(1)
rounds = int(input("How many rounds would you like to play ? "))
time.sleep(1)
print("Great! Let's play ", rounds, "rounds.")
print("")
computer_score = 0
player_score = 0

for round in range(1, rounds + 1):
    player_choice = input(f"Round {round} - Enter your choice (R/P/S): ").upper()
    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "R" and computer_choice == "S") or (player_choice == "P" and computer_choice == "R") or (player_choice == "S" and computer_choice == "P"):
        print("You won this round !")
        player_score += 1
    else:
        print("Computer won this round !")
        computer_score += 1        

    print(f"Score for round {round}: Player {player_score} - Computer {computer_score}")
    time.sleep(1)
    print("Commencing next round...\n")

if player_score > computer_score:
    print(f"Congratulations! You won the game with a score of {player_score} to {computer_score}!")
elif computer_score > player_score: 
    print(f"Computer wins the game with a score of {computer_score} to {player_score}. Better luck next time!")
else:
    print(f"The game is a tie with both scoring {player_score}!")