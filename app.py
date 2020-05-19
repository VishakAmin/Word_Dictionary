import json
from difflib import get_close_matches
n = input("Enter the word :")
data = json.load(open("data.json"))

def transalate(n1):
    n1 = n1.lower()
    if n1 in data:    
        return data[n1]
#to check the title word
    elif n1.title() in data:
        return data[n1.title()]   
    elif n1.upper() in data:
        return data[n1.upper()] 
    elif len(get_close_matches(n1, data.keys()))>0:
        yn = input("Did you mean %s instead. Please press Y if yes and N for no?" %get_close_matches(n1, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(n1, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist .Please Check it" 
        else:
            return "We don't understand Your Entry."           
    else:
        return "The Word Doesn't exist. Please Check it"





output = (transalate(n))


if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)        