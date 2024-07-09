MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money": 0,
}

PRICE = 0

def check_resources(val):
    global PRICE
    require = MENU[val]["ingredients"]
    PRICE = MENU[val]["cost"]
    if require['water'] > resources['water']:
        print("Sorry there is not enough water")
        return False
    elif require.get('milk', 0) > resources.get('milk', 0):
        print("Sorry there is not enough milk")
        return False
    elif require['coffee'] > resources['coffee']:
        print("Sorry there is not enough coffee")
        return False
    else:
        return True


def check_price(quarters = 0,dimes = 0,nickles = 0 ,pennies = 0,val = 0):
    global PRICE
    global resources
    entered_price = 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies
    if entered_price < PRICE:
        print("Sorry that's not enough money. Money refunded.")
    else:
        require = MENU[val]["ingredients"]
        resources['Money'] += PRICE
        resources['water'] -= resources['water']
        resources['milk'] -= resources.get('milk', 0)
        resources['coffee'] -= resources['coffee']

        print(f"Here is ${round(entered_price - PRICE, 2)} in change.")
        print(f"Here is {val}☕. Enjoy !")




machine_on = True
print("Welcome to the coffee machine!")
while machine_on:
    val = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if(val == "off"):
        machine_on = False
    if(val == "report"):
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        if resources['Money'] != 0:
            print(f"Money: {resources['Money']} $")
        
    if(val == "espresso" or val == "latte" or val == "cappuccino") :
        if(check_resources(val)) :
            quarters = int(input("How many quarters : "))  
            dimes = int(input("How many dimes : ")) 
            nickles = int(input("How many nickles : ")) 
            pennies = int(input("How many pennies : "))
            check_price(quarters,dimes,nickles,pennies,val)
        else:
            machine_on: False
