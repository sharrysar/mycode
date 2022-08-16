#!/usr/bin/python3
import os
from cryptography.fernet import Fernet

files = []
path = "/home/student/mycode/finalproject"

# looking for files in the path in path variable
for file in os.listdir(path):
    # ignoring these files
    if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    # add files only to the files list; ignore directories
    if os.path.isfile(file):
        files.append(file)

# opening thekey file and adding the contents to the secretkey variable
with open("thekey.key", "rb") as key:
    secretkey = key.read()

# adding a password to decrypt files
secretphrase = "tlglearning"
# asking for user input for password
user_phrase = input("Enter the password to decrypt the files\n> ")

# conditional statements to check if user gave the right password
# before decrypting the files
if user_phrase == secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        decrypted_contents = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(decrypted_contents)
    print("Your files have been decrypted.")
else:
    print("Wrong password.")
