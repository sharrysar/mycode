#!/usr/bin/python3

# prompt a user for a numeric score
score = int(input("Enter your numeric score: "))

if score >= 90:
    print("Your letter grade is A")
elif score >= 80:
    print("Your letter grade is B")
elif score >= 70:
    print("Your letter grade is C")
elif score >= 60:
    print("Your letter grade is D")
else:
    print("Your letter grade is F. Study more.")