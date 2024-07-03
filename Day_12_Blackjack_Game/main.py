from art import logo
import random

Game_Over = False

def random_value(cards):
    card1 = random.choice(cards)
    card2 = random.choice(cards)
    data = {
        'sum' : card1+card2,
        'cards' : [card1, card2]
    }
    return data

def sum_cards(list) :
    sum = 0
    for i in list :
        sum += i
    return sum

def decision_calculator(user_card, Computer_card) :
    if user_card > 21 :
        print('You went over. You lose ��')
                
    elif(user_card > Computer_card) :
        print('You Win')
                
    elif(user_card < Computer_card) :
        print('You Lose')
                


while not Game_Over:
    decision = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if decision == 'y':
        print(logo)
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        user_card = random_value(cards)
        Computer_card = random_value(cards)
        print('-------------------Your Card-----------------------')
        print(f'Your cards are : {user_card["cards"]}')
        print(f'Your current score is : {user_card["sum"]}')
        print('-------------------Computer Card--------------------')
        print(f'Computer first card : {Computer_card["cards"][0]}')
        print('----------------------------------------------------')
        other_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if other_card == 'n' :
            print(f'Your final hand : {user_card["cards"]}')
            print(f'Your final score : {user_card["sum"]}')

            print(f'Computer first hand : {Computer_card["cards"]}')
            print(f'Computer first score : {Computer_card["sum"]}')
            
            decision_calculator(user_card["sum"] , Computer_card["sum"])
    
        else :
            user_card["cards"].append(random.choice(cards))
            print(f'Your final hand : {user_card["cards"]}')
            print(f'Your final score : {sum_cards(user_card["cards"])}')

            print(f'Computer first hand : {Computer_card["cards"]}')
            print(f'Computer first score : {Computer_card["sum"]}')
            decision_calculator(sum_cards(user_card["cards"]),Computer_card["sum"])
    
        



    else :
        print('Game Over')
        Game_Over = True
