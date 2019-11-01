# data - the donor dictionary file
import json
from difflib import get_close_matches
data = json.load(open("data.json"))

#("\n".join) - for words with >1 meanings
#(get_close_matches) - for typos
def explain(word):
    if word.lower() in data:
        return "\n".join(data[word.lower()])
    elif word.title() in data:
        return "\n".join(data[word.title()])
    elif word.upper() in data:
        return "\n".join(data[word.upper()])
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead?" %get_close_matches(word, data.keys())[0])
        deside = input("Enter y or n: ")
        if deside == "y":
            return "\n".join(data[(get_close_matches(word, data.keys())[0])])
        elif deside == "n":
            return ("Sorry, dictionary doesn't have this word.")
        else:
            return ("You have entered the wrong input. Please enter y or n next time.")
    else:
        return ("Sorry, dictionary doesn't have this word.")

word = input("enter a word to learn its definition: ")
output = explain(word)
print(output)
