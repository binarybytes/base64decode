#!/bin/python3

import base64


print("__________   _______   _____    ")
print("\______   \/  _____/  /  |  |   ")
print(" |    |  _/   __  \  /   |  |_  ")
print(" |    |   \  |__\  \/    ^   /  ")
print(" |______  /\_____  /\____   |   ")
print("        \/       \/      |__|   ")                                         
print("					")
print("     ----------------------------  ") 
print("	      / \ / \ / \ / \ 	")
print("	     ( N | i | k | s ) 	")
print("	      \_/ \_/ \_/ \_/	")
print("	-------------------------")

var = input("Choose one of the following:\n -Decoding:1\n -Encoding:2\n")

def Decode():
    test= input("Enter Base64...")
    data_encoded = base64.b64decode()
    print("\n -------------------------")
    print(data_encoded.decode())
    print("\n")
    input("Press Enter to exit..")

def Encode():
    test = input("Enter text for Encoding...")
    data = base64.b64encode(test.encode())
    print("\n ------------------")
    print(data.decode())
    print("\n")
    input("Press Enter to exit...")

if var == 1:
    Decode()
if var == 2:
    Encode()
else:
    print("Error")
    print("Syntax: <1> or <2>, <encoded text> or <decoded text>")




