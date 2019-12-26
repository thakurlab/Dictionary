import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(w):
	w = w.lower()
	if w in data:
		return data[w]
	elif w.title() in data:
		return data[w.title()]
	elif w.upper() in data:
		return data[w.upper()]
	elif len(get_close_matches(w,data.keys())) > 0:
		yn = input("Did you mean %s ? Enter 1 if yes, or 0 if no : " % get_close_matches(w, data.keys())[0])
		if yn == 1:
			return data[get_close_matches(w, data.keys())[0]]
		elif yn == 0:
			return "The word doesn't exist !!"
		else:
			return "We didn't understand your entry"
	else:
		return "The word doesn't exists ! Please enter another word !"

word = raw_input("Enter the word : " )
output = meaning(word)
print(output)
