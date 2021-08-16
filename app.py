import json
import difflib
from difflib import SequenceMatcher


def getDefinition(q):
    data = json.load(open('data.json'))
    q = q.lower()
    if (q in data):
        return data[q]
    else:
        return 'That word is invalid.'

word = input('Enter a word: ')

print(getDefinition(word))