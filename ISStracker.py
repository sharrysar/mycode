#!/usr/bin/python3
import requests
import time
import reverse_geocoder as rg

url = "http://api.open-notify.org/iss-now.json"

def main():
    # requesting and converting json to python data
    data = requests.get(url).json()
    # putting data in variables to print out
    long = data["iss_position"]["longitude"]
    lat = data["iss_position"]["latitude"]
    # converting epoch time to human readable time
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data["timestamp"]))
    # using reverse_geocoder to translate coords to city
    coords = rg.search((lat, long))
    city = coords[0]["name"]
    country = coords[0]["cc"]

    #printing ISS info
    print(f'''
    CURRENT LOCATION OF THE ISS:
    Timestamp: {timestamp}
    Longitude: {long}
    Latitude: {lat}
    Location: {city}, {country}
    ''')



if __name__ == "__main__":
    main()