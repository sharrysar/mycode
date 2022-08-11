#!/usr/bin/python3
count = 0
# opening the file dracula.txt
with open("dracula.txt", "r") as file:
    with open("vampytimes.txt", "w") as vampy:
    # looping through each line and printing them out
        for line in file:
            if "vampire" in line.lower():
                count += 1
                vampy.write(line)

print(f"Number of occurences: {count}")
            