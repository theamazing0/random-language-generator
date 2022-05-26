import random
import json
from pathlib import Path

def genvowel():
    vowelList = [
        "a",
        "e",
        "i",
        "o",
        "u"
    ]
    return random.choice(vowelList)

def genconsanant():
    consanantList = [
        "b",
        "c",
        "d",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        "m",
        "n",
        "p",
        "q",
        "r",
        "s",
        "t",
        "v",
        "w",
        "x",
        "y",
        "z"
    ]
    return random.choice(consanantList)

def gensyllable():
    length = random.randint(1, 4)
    vowelPlacement = random.randint(1, length)
    vowel = genvowel()
    output = ""
    # print("length: " + str(length))
    # print("vowelPlacement: " + str(vowelPlacement))
    # print("vowel: " + vowel)
    for char in range(length):
        # print("char: " + str(char))
        if char == vowelPlacement-1:
            output += vowel
        elif char != vowelPlacement-1:
            output += genconsanant()
    return output

def genword():
    amount = random.randint(1, 3)
    output = ""
    for syllable in range(amount):
        output += gensyllable()
    return output

# Generate Language
enDictFile = open (str(Path(__file__).parent / "../dictionary/thousand-most-common-words.json"))
enDictList = json.load(enDictFile)
newDict = {}
usedWords = []
counter = 0

for word in enDictList:
    englishWord = (str(word["englishWord"]))
    wordNotRepeated = True
    newWord = genword()
    if newWord not in usedWords:
        newDict[str(englishWord)] = newWord
        usedWords.append(newWord)

print(newDict)