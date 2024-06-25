import random
my_data = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
computer_data = random.randint(0,2)
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''



paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# 0 = rock, 1 = paper, 2 = scissors

if(my_data == 0) :
    print('You chose rock')
    print(rock)
elif(my_data == 1) :
    print('You chose paper')
    print(paper)
elif(my_data == 2) :
    print('You chose scissors')
    print(scissors)

if(computer_data == 0) :
    print('computer chose rock')
    print(rock)
elif(computer_data == 1) :
    print('computer chose paper')
    print(paper)
elif(computer_data == 2) :
    print('computer chose scissors')
    print(scissors)
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