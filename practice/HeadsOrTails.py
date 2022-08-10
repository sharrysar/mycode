#!/usr/bin/python3
# importing random module
import random

print("Flipping the coin....")
flipped = random.randint(0,1)
if flipped == 0:
  print("Heads")
else:
  print("Tails")