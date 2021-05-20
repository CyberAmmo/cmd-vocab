import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def vocab(w):
    if word in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        decition = input(f'Did you mean {get_close_matches(w, data.keys())[0]}? Enter y or n: ')
        if decition == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif decition == 'n':
            return 'Word doesnt exist'
        else:
            return 'Unsuported command!'
    else:
        return 'No such word in'

word = input('Enter a word here: ').lower()

output = vocab(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
