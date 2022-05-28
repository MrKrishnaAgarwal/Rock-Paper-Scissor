# Rock Paper Scissor Game
import random

user_wins= 0
computer_wins= 0

options= ["Rock", "Paper", "Scissor"]

while True:
    user_input= input("Enter Rock, Paper, or Scissors or Q to Quit: ")
    if user_input == "q" or user_input == "Q":
        break

    if user_input not in options:
        continue
    random_number= random.randint(0,2)
    # rock: 0, paper: 1, scissor: 2
    computer_pick= options[random_number]
    print("Computer picked: ", computer_pick + "\n" "You picked: ", user_input)

    if user_input == "Rock" and computer_pick == "Scissor":
        print("You win!")
        user_wins += 1

    elif user_input == computer_pick:
        print("It's a tie!")
        
    elif user_input == "Paper" and computer_pick == "Rock":
        print("You win!")
        user_wins += 1

    elif user_input == "Scissor" and computer_pick == "Paper":
        print("You win!")
        user_wins += 1

    else:
        print("You lose!")
        computer_wins += 1
print("You won: ", user_wins, "times.")
print("Computer won: ", computer_wins, "times.")
if user_wins > computer_wins:
    print("You are the winner!")
elif user_wins < computer_wins:
    print("Computer is the winner!")
else:
    print("It's a tie!")
print ("Thanks for playing!")