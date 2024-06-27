import random
print('Welcome to the PyPassword Generator!')
print('How many letters would you like in your password?')
letters = int(input())
print('How many symbols would you like?')
symbols = int(input())
print('How many numbers would you like?')
numbers = int(input())

capital_alphabets = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


special_characters = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', 
    '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', 
    ',', '.', '?', '/', '~', '`'
]


t_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

data = []
for capital_alphabet in range(0,letters) :
    data.append(random.choice(capital_alphabets))
for special_character in range(0,symbols) :
    data.append(random.choice(special_characters)) 
for t_number in range(0,numbers) :
    data.append(random.choice(t_numbers))

random.shuffle(data)
password = ''
for value in data :
     password += value
print(f'The password is {password}')