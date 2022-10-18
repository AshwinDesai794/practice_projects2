import data_coffeeType
from data_coffeeType import MENU, resources

profit = 0
is_on = True


def is_resource_sufficient(order_ingredients):
    """Returns if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry theres not enough {item}")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted!!"""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is the change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources """
    for item in order_ingredients:
        resources[item] = resources[item] - order_ingredients[item]
    print("Here is your Drink")


while is_on:
    choice = input("What would you like to have? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        # print(resources)
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}ml")
        print(f"Money : ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):  # if this condition is true
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(drink_name=choice, order_ingredients=drink["ingredients"])
