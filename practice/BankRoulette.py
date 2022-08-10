#!/usr/bin/python3
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma.\n>")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

nameslen = len(names)
payer = random.randint(0, nameslen-1)
print(f"{names[payer]} will be paying!")
