from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
latte = MenuItem("latte",200,150,24,2.50)
espresso = MenuItem("espresso",50,0,18,1.50)
cappuccino = MenuItem("cappuccino",250,100,24,3.00)
items = [latte, espresso, cappuccino]

on = True
while on:
    user_drink = input(f"What would you like? {menu.get_items()}: ").lower()
    
    if user_drink == 'off':
        on = False
    elif user_drink == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        choice = menu.find_drink(user_drink)
        if coffee_maker.is_resource_sufficient(choice) and money_machine.make_payment(choice.cost):
            coffee_maker.make_coffee(choice)