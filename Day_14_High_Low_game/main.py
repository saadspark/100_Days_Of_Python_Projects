from art import logo
from art import vs
from game_data import data
import random

def generate_random():
    random_number = random.randint(0, len(data) - 1)
    return data[random_number]

def check(val, person_one, person_two):
    global game_over
    global high_score
    if val == "a" and person_one["follower_count"] > person_two["follower_count"]:
        print("A is the winner")
        high_score += 1
        return high_score
    elif val == "b" and person_two["follower_count"] > person_one["follower_count"]:
        print("B is the winner")
        high_score += 1
        return high_score
    else:
        print("You lose")
        game_over = True
        

game_over = False
high_score = 0

print(logo)
print("Welcome to the higher lower game")

while not game_over:
    person_one = generate_random()
    person_two = generate_random()

    while person_one == person_two:
        person_two = generate_random()

    print(f'Compare A: {person_one["name"]}, a {person_one["description"]} from {person_one["country"]}')
    print(vs)
    print(f'Against B: {person_two["name"]}, a {person_two["description"]} from {person_two["country"]}')

    selector = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    if check(selector, person_one, person_two):
        print(f"Current score: {high_score}")
    else:
        print(f"Final score: {high_score}")
