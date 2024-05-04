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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Money: ${profit}")


def is_resources_sufficient(ingredients):
    for resource in ingredients:
        if ingredients[resource] > resources[resource]:
            print(f"Sorry not enough {resource}")
            return False
    return True


def process_coins():
    try:
        print("Please insert coins.")
        total = float(input("How much quarters:\n> ")) * 0.25
        total += float(input("How much dimes:\n> ")) * 0.10
        total += float(input("How much nickles:\n> ")) * 0.05
        total += float(input("How much pennies:\n> ")) * 0.01
        return total
    except ValueError:
        print("\nThis coin is invalid.")
        print("All money refunded.")
        return process_coins()


def is_transaction_successful(payment, drink_cost):
    global profit
    if payment >= drink_cost:
        print(f"Coffee Price: ${round(drink_cost, 2)} You paid: ${round(payment, 2)} Here is your ${round(payment-drink_cost, 2)} in change.")
        profit += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(coffee, ingredients):
    for resource in ingredients:
        resources[resource] -= ingredients[resource]
    return print(f"Here is your {coffee.capitalize()}.")


coffee_machine = True
while coffee_machine:
    choice = input("What would you like? (espresso/latte/cappuccino):\n>")
    try:
        if choice == "off":
            coffee_machine = False
        elif choice == "report":
            report()
        else:
            drink = MENU[choice]
            if is_resources_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
    except KeyError:
        continue
