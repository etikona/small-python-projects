# Ask the user to make the choice
# If choice is not valid
#   print an Error
# Let the computer to make the choice
# Print choice with (emojis)
# Determine the winner
# Ask the user if they want to continue
# If not
# Terminate

# import random

#* Refactoring: Modularizing Code
# emojis = {'r': 'rock', 's': 'scissor', 'p': 'paper'} # Dictionary
# choices = ('r', 's', 'p')

# def get_user_choice():
#     while True:
#         user_choices = input("Rock, Paper or Scissors ? (r/p/s) : ").lower()
#         if user_choices  in choices:
#            return user_choices 
#         else:
#             print("Invalid Choice")

# def display_choices (user_choices, computer_choice):
    
#     print(f'You choose', {emojis[user_choices]})     
#     print(f'You choose', {emojis[computer_choice]})  

# def determine_winner (user_choices, computer_choice):
#     if user_choices == computer_choice :
#         print("Tie.")
#     elif (user_choices == 'r' and computer_choice == 's') or (user_choices == 'p' and computer_choice == 'r') or (user_choices == 's' and computer_choice == 'p')  :
#         print("You win")  
#     else:
#         print("You Lose")


# def play_game():
#     while True :
#         user_choices = get_user_choice()

#         computer_choice = random.choice(choices)
#         display_choices(user_choices, computer_choice)
#         determine_winner(user_choices, computer_choice)
    

#         should_continue = input("You wanna continue ? (y/n) : ").lower()
#         if should_continue == 'n':
#             break
#         else:
#             continue

# play_game()

#*  Refactoring: Applying the DRY Principle

import random


ROCK="r"
PAPER="p"
SCISSOR="s"
emojis = {ROCK: 'rock', SCISSOR: 'scissor', PAPER: 'paper'} # Dictionary
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choices = input("Rock, Paper or Scissors ? (r/p/s) : ").lower()
        if user_choices  in choices:
           return user_choices 
        else:
            print("Invalid Choice")

def display_choices (user_choices, computer_choice):
    
    print(f'You choose', {emojis[user_choices]})     
    print(f'Computer choose', {emojis[computer_choice]})  

def determine_winner (user_choices, computer_choice):
    if user_choices == computer_choice :
        print("Tie.")
    elif (user_choices == ROCK and computer_choice == SCISSOR) or (user_choices == PAPER and computer_choice == ROCK) or (user_choices == SCISSOR and computer_choice == PAPER)  :
        print("You win")  
    else:
        print("You Lose")


def play_game():
    while True :
        user_choices = get_user_choice()

        computer_choice = random.choice(choices)
        display_choices(user_choices, computer_choice)
        determine_winner(user_choices, computer_choice)
    

        should_continue = input("You wanna continue ? (y/n) : ").lower()
        if should_continue == 'n':
            break
        else:
            continue

play_game()