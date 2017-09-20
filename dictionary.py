import json
from difflib import get_close_matches as match

data = json.load(open("data.json",'r'))

#creating function "search" to search and describe the word given by the user
def search(word):
    #lowering the word given by the user, so the capital letters will be irrelevant
    word = word.lower()
    #trying to understand the word user provide by matching it with existing ones
    missType = match(word, data.keys(), cutoff=0.8, n=1)
    #checking if the word exists
    if word in data:
        return data[word]
    elif len(missType) > 0:
        print ("\nDid you mean %s instead?" % missType[0])
        decision = input("\nType 'Y' to accept %s, or type 'N' to enter another word: " % missType[0])
        decision = decision.lower()
        if decision == "y":
            #changing the global variable of input so the print statement will show the right-spelled word
            global w
            w = missType[0]
            return data[missType[0]]
        elif decision == "n":
            return "Ok, let's try another word."
        else:
            return "Doesn't understand your entry"
    else:
        return "The word doesn't exist. Please double check it "

#gathering input from user in an inifnite loop
while True:
    w = input("Enter word or type 'finito' to exit the program:  ")
    #can't exit the program by a simple word because our dictionary comtain thjem all
    if w == "finito": break
    output = search(w)
    #function is returning list and string so checking whether it is list or string
    if type(output) == list:
        for item in output:
            print ("\n%s: \n" % w.upper(),item)
    else:
        print ("\n%s: \n" % w.upper(),output)
