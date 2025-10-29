#Loop
# Ask: roll the dice?
# If user enters y
#  Generate two random numbers
#  print them
# If user enters n
#   Print thank you message
#   Terminate the program
# Else
#  print Invalid choice

import random

while True:
    choice = input("Roll the dice? (y/n) : ").lower()
    if choice == 'y':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f' ({dice1}, {dice2}) ')

    elif choice == 'n':
        print("Thank you for playing") 
        break
    else:
        print("Invalid choice")   

