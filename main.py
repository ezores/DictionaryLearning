#Simple dictionary program to help me understand Python

#data.json contains the dictionary data to use for the program
import json as js
import difflib
data = js.load(open("data.json"))
#print(data) # testing if it works

def translate(toSearch):
  toSearch = toSearch.lower()
  if toSearch in data:
    return data[toSearch]
  elif toSearch.title() in data:
    return data[toSearch.title()]
  elif toSearch.upper() in data:
    return data[toSearch.upper()]
  elif len(get_close_matches(toSearch, data.keys())) > 0 :
      print("Did you mean %s instead of: " %get_close_matches(toSearch,data.keys())[0])
  else:
    print("The entered word does not match our records! Please try again ")



toSearch = input("Enter the word you would like to search: ")
output = translate(toSearch)
if type(output) == list:
  for item in output:
    print(item)
else:    
  print(output)