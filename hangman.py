import json
from random import choice

def newSequence(char, word, NewWord):
    indices = [i for i,j in enumerate(word) if j==char]
    sequence = [letter for letter in NewWord]
    for i in indices:
        sequence[i] = char
    return "".join(sequence)

jsonFile = open('words.json')
word_list = json.load(jsonFile)
word = choice(word_list["data"])

print(f"You have 3 chances to guess the word correctly")
print("Word:", end=" ")
print("-"*len(word))
guess = input("Enter character: ")
chance = 0

NewWord = "-"*len(word)
while True:
    print()
    print("="*20)
    print()
    if len(guess) == 1:
        if guess in word:
            NewWord = newSequence(guess, word, NewWord)
            print("Word:", NewWord)
            if NewWord == word:
                print("You guessed the correct word!!")
                break
        else:
            print('your guess is wrong')
            chance+=1
            if chance==3:
                print("You lost")
                print("Word was:", word)
                break
            print("Remaining chances: ",3-chance)
        guess = input("Enter next character: ")
    else:
        print("Enter only one character")
        guess = input("Enter character: ")
