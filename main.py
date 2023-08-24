from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
on=True
while(on):
    a=input("What would you like? (espresso/latte/cappuccino/):")
    if a=="off":
        on=False
    elif a=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        if coffee_maker.is_resource_sufficient(menu.find_drink(a)):
            if money_machine.make_payment(menu.find_drink(a).cost):
                coffee_maker.make_coffee(menu.find_drink(a))



