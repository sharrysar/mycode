#!/usr/bin/python3
# program that prints out the actor playing the role
# ie: Kit Harrington as Jon Snow
import requests
import crayons

def main():

    while True:
        # url doesnt accept a whitespace so replacing whitespace in input to +
        name = input("Which character would you like to check?\n")
        name = name.replace(" ", "+")
        # api request
        url = f"https://anapioficeandfire.com/api/characters/?name={name}"   

        #converting json to python data
        data = requests.get(url).json()

        try:
            print(f''' 
            {data[0]["name"]} aka {data[0]["titles"][0]} is played by the actor {data[0]["playedBy"][0]}!
            ''')

        except:
            print(crayons.red("There is no character of that name. Try their full name!\n"))


if __name__ == "__main__":
    main()