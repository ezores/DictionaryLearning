#Simple dictionary program to help me understand Python

#data.json contains the dictionary data to use for the program
import json as js

data = js.load(open("data.json"))

print(data) # testing if it works