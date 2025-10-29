# Generate a random number
# Ask the user to make a guess
# If not a valid number
#   print an error
# If number < guess
#   print too low.
# If number > guess
#   print too high
# Else
# print well done.

#! https://docs.google.com/document/d/1rFeU0gmRlt6jY3yEghOgC6aqM1wLOSo6fcKljKi0tq0/edit?fbclid=IwY2xjawNvBo9leHRuA2FlbQIxMABicmlkETF6SGRvNHRLaEZGdHNnZTBtAR61gd245zzQMrKx3es5_kh5dGhp6aT2Z00scYZ58prtkPLBZSW4vmZBAwGaVw_aem_vAR7bGPdTrsoXqebGuL0OA&tab=t.0#heading=h.vwn8sszajmxr
import random


number_to_guess = random.randint(1, 100)

while True:
 try:
    guess = int(input("Guess the number between 1 to 100 :"))

    if guess < number_to_guess:
        print("Too low..!")
    elif guess > number_to_guess:
        print("Too high..!")  
    else:
        print("well done, you guess the right")    
        break
 except  ValueError:
    print("Please enter a valid number")
