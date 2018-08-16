import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def dic(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif w.title() in data:
        return data[w.title()]
    elif len(get_close_matches(word,data.keys()))> 0:
        yn= input("Did you mean %s instead? Enter Y for yes,or N for No: " % get_close_matches(word, data.keys())[0])
        if yn=="Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn=="N":
            return "The word doesn't exit.Please enter again.."
        else:
            return "The word doesn't exit..."
    else:
       return "The word doen't exit. Please recheck the word "


word=input("Enter word: ")
output=dic(word)

if type(output)==list:
    for item in output:
        print(item)
else:
  print(output)
