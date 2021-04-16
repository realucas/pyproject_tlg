#!/usr/bin/env python3

"""Ricky Lucas || Making a custom if elif else program"""

import random

ranum1 = random.randint(0,5)
ranum2 = random.randint(0,5)
print(f"Welcome to High or Low!! the current number is: {ranum1} ")

if ranum2 > ranum1:
    status = "h"
    result = "High"
elif ranum2 < ranum1:
    status = "l"
    result = "Low"
else:
    status = "t"
    result = "Tie"
print("Is the next number High, Low or Tie: ")

while (True):
    playerinput = input("High: h\n Low: l\n Tie: t\n Answer: ")
    print("Invalid entry! Try again!")  
    if (playerinput == 'h' or 'l' or 't'):
        break
       
print(f"The next number is {ranum2} - {result} ")

if playerinput == status:
    message = "You win!"
else:
    message = "Lewhewzeher!"
print(message)

