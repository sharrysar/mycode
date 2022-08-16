#!/usr/bin/python3
import os
from cryptography.fernet import Fernet

files = []
path = "/home/student/mycode/testfiles"

for file in os.listdir(path):
    if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("thekey.key", "rb") as key:
    secretkey = key.read()

secretphrase = "tlglearning"

user_phrase = input("Enter the password to decrypt the files\n> ")

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
