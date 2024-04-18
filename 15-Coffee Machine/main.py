from data import MENU, resources

profit = 0


def report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${profit}")
    return


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:

            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def is_transaction_successful(user_choice, total):
    if total >= MENU[user_choice]["cost"]:
        change = total - MENU[user_choice]["cost"]
        global profit
        profit += MENU[user_choice]["cost"]
        print(f"Here is ${round(change, 2)} dollars in change.")
        return True
    else:
        return False


is_on = True
while is_on:
    coins = {}
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        is_on = False
    print("Please insert coins.")
    if user_choice == "report":
        report()
    if user_choice not in MENU:
        print("Invalid choice. Please choose espresso, latte, or cappuccino.")
    else:
        coins["quarters"] = int(input("How many quarters?: "))
        coins["dimes"] = int(input("How many dimes?: "))
        coins["nickels"] = int(input("How many nickels?: "))
        coins["pennies"] = int(input("How many pennies?: "))

        coin_values = {
            "quarters": 0.25,
            "dimes": 0.10,
            "nickels": 0.05,
            "pennies": 0.01,
        }
        total = round(sum(coins[coin] * coin_values[coin] for coin in coins), 2)
        print(f"Total value of coins: ${total}")

        if is_resource_sufficient(MENU[user_choice]["ingredients"]):
            if is_transaction_successful(user_choice, total) == True:
                make_coffee(user_choice, MENU[user_choice]["ingredients"])
            else:
                print("Sorry that's not enough money. Money refunded.")
