#Step 4

import random
from hangman_art import logo
from hangman_words import word_list
from hangman_art import stages
end_of_game = False

chosen_word = random.choice(word_list)
word_length = len(chosen_word)


live = 6

print(logo)
print("Welcome to the Hangman game!")

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        
    if guess not in chosen_word:
        live -= 1
       
    if live == 0 :
        end_of_game = True
        print("You lose.")
        print(f"The word was {chosen_word}")
   
    print(f"{' '.join(display)}")
    if "_" not in display:
        print("You win.")

    print(stages[live])
    