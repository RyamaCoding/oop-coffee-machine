# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon", ["Pikachu", "Bulbasaur", "Charizard"])
# table.add_column("Primary Type", ["Electric", "Grass", "Fire"])
# table.align = "l"
#
# print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    machine_is_on = True
    
    while machine_is_on:
        coffee_choice = input(f"What coffee would you like today? ({menu.get_items()}): ")
        
        if coffee_choice == "off":
            print("Turning off the machine. Goodbye!")
            machine_is_on = False
            
        elif coffee_choice == "report":
            coffee_maker.report()
            money_machine.report()
            
        else:
            drink = menu.find_drink(coffee_choice)
            if drink:
                if coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)

        if coffee_maker.resources["water"] == 0 or coffee_maker.resources["milk"] == 0 or coffee_maker.resources["coffee"] == 0:
            print("Sorry, the machine is out of resources. Turning off.")
            machine_is_on = False

main()