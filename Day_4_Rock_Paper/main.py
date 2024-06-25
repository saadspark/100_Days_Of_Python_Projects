import random
my_data = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
computer_data = random.randint(0,2)
if my_data == computer_data :
    print('It\'s a draw.')
elif my_data == 0 and computer_data == 2 :
    print('You win.')
elif my_data == 1 and computer_data == 0 :
    print('You win.')
elif my_data == 2 and computer_data == 1 :
    print('You win.')
elif my_data == 0 and computer_data == 1 :
    print('You lose.')
elif my_data == 1 and computer_data == 2 :
    print('You lose.')
elif my_data == 2 and computer_data == 0 :
    print('You lose.')
else :
    print('You typed an invalid number, you lose.')