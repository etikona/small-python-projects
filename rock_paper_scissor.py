# Ask the user to make the choice
# If choice is not valid
#   print an Error
# Let the computer to make the choice
# Print choice with (emojis)
# Determine the winner
# Ask the user if they want to continue
# If not
# Terminate

import random

emojis = {'r': '🥌', 's': '✂', 'p': '📄'} # Dictionary
choices = ('r', 's', 'p')

while True :
    user_choices = input("Rock, Paper or Scissors ? (r/p/s) : ").lower()
    if user_choices not in choices:
        print("Invalid choice")
        continue

    computer_choice = random.choice(choices)

    print(f'You choose', {emojis[user_choices]})     
    print(f'You choose', {emojis[computer_choice]})     

    if user_choices == computer_choice :
        print("Tie.")
    elif (user_choices == 'r' and computer_choice == 's') or (user_choices == 'p' and computer_choice == 'r') or (user_choices == 's' and computer_choice == 'p')  :
        print("You win")  
    else:
        print("You Lose")

    should_continue = input("You wanna continue ? (y/n) : ").lower()
    if should_continue == 'n':
        break
    else:
        continue

