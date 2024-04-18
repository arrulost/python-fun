from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()


is_on = True
while is_on:
    user = input(f"What would you like? ({menu.get_items()}) ").lower()
    if user == "off":
        is_on = False
    elif user == "report":
        coffeemaker.report()
        moneymachine.report()
    else:
        drink = menu.find_drink(user)
        if drink is not None:
            if coffeemaker.is_resource_sufficient(drink) and moneymachine.make_payment(drink.cost):
                    coffeemaker.make_coffee(drink)
