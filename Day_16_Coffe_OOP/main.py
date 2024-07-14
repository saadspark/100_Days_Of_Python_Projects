from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print("Welcome to the Coffee Machine!")
main = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()



get_coffee= True
while get_coffee:
    name = input(main.get_items())
    if name == "off":
        get_coffee = False
    if name == "report":
        coffee_maker.report()
        money_machine.report()
    if main.find_drink(name) and coffee_maker.is_resource_sufficient(name):
            print(f"We have {name} available.")
            coin = money_machine.process_coins()
            if(money_machine.make_payment(coin)) :
                print(f"Here is {name}☕. Enjoy !")

    else:
        print(f"Sorry, we don't have {name} in our menu.")
        get_coffee = False
