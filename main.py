import os
from hangman_pic import hangman_pics
from hangman_words import words_list
import random

def clear():
    """
    Clears the terminal screen and scroll back to present
    the user with a nice clean, new screen. Useful for managing
    menu screen in the terminal applocations.
    """
    os.system('cls||echo -e \\\\033c')

words_list = words_list
word = random.choice(words_list)
word_length = len(word)
blank_list = []
for _ in range(word_length):
    blank_list.append('_')

endgame = False
total = 0
while endgame == False:
    guess = input('Enter a letter --> ').lower()
    clear()
    if guess in blank_list:
        print(f"You've already guessed this letter {guess}")
    if guess not in word:
        print(hangman_pics[total])
        print(f"You guessed '{guess}'. that's not in the word, therefore you loose a life!")
        total += 1
    for i in range(word_length):
        if word[i] == guess:
            blank_list[i] = guess
    print(' '.join(blank_list))
    print()

    if '_' not in blank_list:
        print("You have successfully filled all the blanks")
        print('You WIN!! 😁')
        endgame = True

    if total == len(hangman_pics):
        print("Hangman is Dead!, You LOOSE!!")
        print(f"The word was --> {word}")
        endgame = True