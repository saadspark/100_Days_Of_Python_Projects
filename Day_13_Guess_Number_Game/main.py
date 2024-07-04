from art import logo
import random
print(logo)     
Easy = 10
Hard = 5
VAL_TO_GUESS = random.randint(1, 100)
print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")
val = input("Choose a difficulty. Type 'easy' or 'hard':")
val_to_guess = random.randint(1, 100)
if val == 'easy':
    attempts = Easy
else:
    attempts = Hard

print(VAL_TO_GUESS)

def Check(val):
    if val > VAL_TO_GUESS:
        print('Too high.')
        return False
    elif val < VAL_TO_GUESS:
        print('Too low.')
        return False
    else:
        print('You got it.')
        return True
    

val_remaining = attempts+1

for i in range(1,val_remaining) :
    val_remaining -= 1
    print(f'You have {val_remaining} attempts remaining to guess the number.')
    val = int(input('Make a guess:'))
    Check(val)


