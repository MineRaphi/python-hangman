# Python Hangman by Raphael Zadny
import random
import sys

with open('words.txt') as f:        # Imports the wordlist from "words.txt"
    words = f.read().splitlines()   

guessed = []
wrong = []
revealed = ["_"] * 5

def getWord():
    global word
    global wordList
    global wordLen
    word = words[random.randint(0, len(words)-1)]   # Selects a word from the wordlist
    wordList = list(word)
    wordLen = len(wordList)

def guess():
    usr = input("Take a guess: ")   # Askes the user for a guess
    if len(list(usr)) != 1:
        print("Guess can only have one letter!")
    elif usr in guessed:
        print("You can not guess a letter twice")
    else:
        guessed.append(usr)
        if usr in wordList:
            x = 0
            while x != wordLen:
                if wordList[x] == usr:
                    revealed[x] = usr
                x += 1
            print(" ".join(revealed))
        else:
            print("incorrect")
            print(" ".join(revealed))
            wrong.append(usr)
            if len(wrong) == 11:
                print("You lose")
                print("The word was:" + " ".join(wordList))
                exit()
    if revealed == wordList:
        print("You win")
    else:
        guess()

getWord()
revealed = ["_"] * wordLen
print(" ".join(revealed))
guess()