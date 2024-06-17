
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
}

money = 0
transaction_success = False
# 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
    #a. Check the user’s input to decide what to do next.
    #b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.

user_input = input("What would yo like? (espressso/latte/cappuccino): ")

# 2. Turn off the Coffee Machine by entering “​off”​to the prompt.
    #a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. Your code should end execution when this happens.

machine_ON = True

# 3. Print report.
    #a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
        #Water: 100ml
        #Milk: 50m l
        #Coffee: 76g
        #Money: $2.5
def print_report():
    print(f" Water: {resources['water']}ml ")
    print(f" Milk: {resources['milk']}ml ")
    print(f" Coffee: {resources['coffee']}g ")
    print(f" Money: ${money} ")



# 4. Check resources sufficient?
    #a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
    #b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “​Sorry there is not enough water.”​
    #c. The same should happen if another resource is depleted, e.g. milk or coffee.

#print(MENU['latte']['ingredients']['water'])

def check_resources(input):
    if {resources['water']} < {MENU[input]['ingredients']['water']}:
        print("​Sorry there is not enough water.")
    elif {resources['milk']} < {MENU[input]['ingredients']['milk']}:
        print("​Sorry there is not enough milk.")
    elif {resources['coffee']} < {MENU[input]['ingredients']['coffee']}:
        print("​Sorry there is not enough coffee.")
    else:
        print(f"Insert ${MENU[input]['cost']} for {input}")


# 5. Process coins.
    #a. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
    #b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    #c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
def process_coins():
    
    Quarters = int(input("How many Quarters you want to input: "))
    Dimes = int(input("How many Dimes you want to input: "))
    Nikles = int(input("How many Nikles you want to input: "))
    Pennies = int(input("How many Pennies you want to input: "))

    quarters = Quarters * 0.25
    dimes = Dimes * .10
    nikles = Nikles * 0.05
    pennies = Pennies * 0.01

    total = quarters+dimes+nikles+pennies
    return total

#print(process_coins())
# 6. Check transaction successful?
    #a. Check that the user has inserted enough money to purchase the drink they selected. E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say “​Sorry that's not enough money. Money refunded.​”.
    #b. But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. E.g. Water: 100ml
        # Milk: 50ml
        # Coffee: 76g
        # Money: $2.5
    #c. If the user has inserted too much money, the machine should offer change.
        #E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.

def transaction(input):
    global money, transaction_success
    total = process_coins()
    if total < MENU[input]['cost']:
        print("Sorry that is not enough money. Money refunded")
    elif total > MENU[input]['cost']:
        change = round(total,2) - round(MENU[input]['cost'],2)
        print(f"Cost of {input} is ${MENU[input]['cost']} dollars. Here is ${round(change,2)} dollars in change you paid extra.")
        money += (total - change)
        transaction_success = True
        return money, transaction_success
    else:
        money += (total - change)
        transaction_success = True
        return money, transaction_success

#print_report()
# 7. Make Coffee.
    #a. If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
        #E.g. report before purchasing latte: Water: 300ml
                                            # Milk: 200ml
                                            # Coffee: 100g
                                            # Money: $0
            # Report after purchasing latte:
                                            # Water: 100ml
                                            # Milk: 50ml
                                            # Coffee: 76g
                                            # Money: $2.5
    #b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.

def make_coffee(input):
    global transaction_success
    if transaction_success:
        resources["water"] = resources["water"] - MENU[input]["ingredients"]["water"]
        print(f"Here is your {input}. Enjoy!")
    else:
        return

def operation(input):
    while machine_ON:
        if input != 'Off':
            print_report()
            check_resources(input = user_input)
            transaction(input= user_input)
            make_coffee(input = user_input)
        else:
            return




