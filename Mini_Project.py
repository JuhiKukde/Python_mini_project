# Guess The Number

import random

number = random.randint(1,100)

while True:
    userChoice = input("Guess the Number  or Quite :  ")
    if(userChoice == "Exit"):
        break

    userChoice = int(userChoice)
    if(userChoice == number):
        print("Success : Corect Guess")
        break
    elif(userChoice < number):
        print(" You number was too small. Take a bigger guess")
    else:
        print(" Your number was too big . Take a smaller guess")

print( "-----Game Over ----- ")




# Random Password Generator

import random
import string

pass_len = 6
charVal = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += (random.choice(charVal))

print("Your random password is " ,password )
