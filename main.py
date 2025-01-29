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

# Function to update resources
def update_resources(drink):
    drink_resources = MENU[drink]['ingredients']
    for x in drink_resources:
        if resources[x] < drink_resources[x]:
            print(f"Sorry there is not enough {x}.")
            return False
    for x in drink_resources:
        resources[x] -= drink_resources[x]
    return True

# Function to handle making the drink
def make_drink(user_choice):
    global profit
    if user_choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
        return False
    elif user_choice in MENU:
        if update_resources(user_choice):
            print(f"Your {user_choice} is being prepared.")
            return True
        else:
            return False
    else:
        print("Invalid choice.")
        return False

# Main game loop
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        is_on = False
    else:
        # Check if the drink can be made
        can_make_drink = make_drink(choice)

        if can_make_drink:
            # Ask for money if the drink can be made
            print("Please insert coins.")
            quarters = float(input("How many quarters?: ")) * 0.25
            dimes = float(input("How many dimes?: ")) * 0.10
            nickles = float(input("How many nickles?: ")) * 0.05
            pennies = float(input("How many pennies?: ")) * 0.01
            inserted_amount = quarters + dimes + nickles + pennies

            drink_cost = MENU[choice]['cost']
            if inserted_amount >= drink_cost:
                change = round(inserted_amount - drink_cost, 2)
                print(f"Here is ${change} in change.")
                print(f"Here is your {choice}. Enjoy!")
                profit += drink_cost
            else:
                print(f"Sorry, that's not enough money. ${inserted_amount} refunded.")
                # Refund resources since the drink was not made
                for ingredient in MENU[choice]['ingredients']:
                    resources[ingredient] += MENU[choice]['ingredients'][ingredient]