#!/usr/bin/python3
# importing 3rd party libs
import argparse
import requests
import pandas

# pokemon API url
URL = "http://pokeapi.co/api/v2/item/"

# defining main fx
def main():
    # get request to api -- limit only 1k items
    items = requests.get(f"{URL}?limit=1000")
    items = items.json()

    # a list to store items with the searched word
    matchedwords = []

    # loop thru data and print pokemon names
    for item in items.get("results"):
        if args.searchword in item.get("name"):
            matchedwords.append(item.get("name"))

    finishedlist = matchedwords.copy()
    matchedwords = {}
    matchedwords["matched"] = finishedlist

    print(f"There are {len(finishedlist)} words that contain the word '{args.searchword}' in the Pokemon Item API!")
    print(f"List of Pokemon items containing '{args.searchword}': ")
    print(matchedwords)

    ## export to excel with pandas
    # make a dataframe from our data
    itemsdf = pandas.DataFrame(matchedwords)
    # export to MS Excel XLSX format
    # run the following to export to XLSX
    # python -m pip install openpyxl
    # index=False prevents the index from our dataframe from
    # being written into the data
    itemsdf.to_excel("pokemonitems.xlsx", index=False)

    print("Gotta catch 'em all!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pass in a word to search\
    the Pokemon item API")
    parser.add_argument('searchword', metavar='SEARCHW',\
    type=str, default='ball', help="Pass in any word. Default is 'ball'")
    args = parser.parse_args()
    main()