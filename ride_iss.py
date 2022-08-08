#!/usr/bin/python3
# tracking the iss using an API

import requests

# defining URL
MAJORTOM = "http://api.open-notify.org/astros.json"

def main ():
    # calling the webservice and will return 200 ok
    groundctrl = requests.get(MAJORTOM)
    # translating the json into a python list
    helmetson = groundctrl.json()

    # display python data
    print("\n\nConverted Python data")
    print(helmetson)

    print("\n\nPeople in Space: ", helmetson['number'])
    people = helmetson["people"]
    for astronaught in people:
        print(astronaught["name"] + "on the " + astronaught["craft"])

if __name__ == "__main__":
    main()