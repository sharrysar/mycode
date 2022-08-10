#!/usr/bin/python3

while True:
    try:
        print("Enter a filename: ")
        name= input()
        with open(name, "w") as myfile:
            myfile.write("No problems with that filename")
        break
    except:
        print("Error with that filename! Try again...")