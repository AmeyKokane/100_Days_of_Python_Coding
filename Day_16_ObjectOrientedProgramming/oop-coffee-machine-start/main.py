from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



# 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
    #a. Check the user’s input to decide what to do next.
    #b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True



while is_on:
    order = input(f"What would yo like? ({menu.get_items()}): ")
    if order == "off":
        is_on = False
    elif order == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

# 2. Turn off the Coffee Machine by entering “​off”​to the prompt.
    #a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the
    #   machine. Your code should end execution when this happens.
