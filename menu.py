import math
from item import Item
import os

class Menu():

    list_of_items = []
    line = "="*25
    title = ""

    def __init__(self, title = ""):
        self.title = title
    
    def show_menu(self):
        os.system("clear")
        print(self.line)
        print(math.floor(len(self.line)/2-len(self.title)/2)*" "+self.title)
        print(self.line+"\n")
        print("1. Add Item")
        print("2. Show List")
        print("3. Edit Item\n")
        print("4. Quit")
        ans = self.validate_input(input("\n> "), 4)
        if ans == 1:
            self.add_item(self.input_item())
            self.show_menu()
        if ans == 2:
            self.show_items()
            self.show_menu()
        if ans == 3:
            self.show_edit_menu()
            self.show_menu()
        if ans == 4:
            pass
    
    def validate_input(self, ans, option_range):
        try:
            ans = int(ans)
            if option_range and range(option_range)[ans]:
                return ans
        except:
            return self.validate_input(input("\nPlease input a valid option...\n> "))

    def validate_num(self, num):
        try:
            num = int(num)
            return num
        except:
            return self.validate_num(input("\nPlease enter valid number: \n\n> "))

    def validate_price(self, price):
        try:
            if "." in price:
                price = price.replace(".", "")
            else:
                price = price + "00"
            price = int(price)
            return price
        except:
            return self.validate_price(input("\nPlease enter valid price: \n\n> $"))

    def input_item(self):
        name = input("\nInput the item name: \n\n> ")
        amount = self.validate_num(input("\nInput the amount of items: \n\n> "))
        print(amount)
        price = self.validate_price(input("\nInput the price of each item: \n\n> $").replace("$", ""))
        print(price)
        return Item(name, price, amount)

    def add_item(self, item):
        for i in self.list_of_items:
            if i.get_name().lower() == item.get_name().lower() and i.get_price() == item.get_price():
                i.set_amount(i.get_amount + item.get_amount())
                return
        self.list_of_items.append(item)
    
    def show_items(self):
        iteration = 0
        total = 0
        if len(self.list_of_items) <= 0:
            print("\nList is empty...")
            input("\nPress enter to continue...")
            return
        print()
        for i in self.list_of_items:
            print("{}. {} {} (${price_per:.2f} per): ${price_total:.2f}".format(str(iteration+1), i.get_amount(),
                                                                                i.get_name(), price_per=i.get_price()/100, price_total=i.get_total_price()/100))
            total = total + i.get_total_price()
            iteration = iteration + 1
        print("\nTotal: ${total:.2f}".format(total=total/100))
        input("\nPress enter to continue...")

    def show_edit_menu(self):
        iteration = 0
        if len(self.list_of_items) <= 0:
            print("\nNothing to edit...")
            input("\nPress enter to continue...")
            return
        print()
        for i in self.list_of_items:
            print("{}. {} {} (${price_per:.2f} per): ${price_total:.2f}".format(str(iteration+1), i.get_amount(),
                                                                                i.get_name(), price_per=i.get_price()/100, price_total=i.get_total_price()/100))
            iteration = iteration + 1
        ans = self.validate_num(input("\nWhat item would to edit?: \n\n> "))
        if ans-1 <= len(self.list_of_items):
            item = self.list_of_items[ans-1]
            self.edit_item(item)
    
    def edit_item(self, item):
        os.system("clear")
        print("\nWhat would you like to edit? ({} {} (${price_per:.2f} per): ${price_total:.2f})".format(
            item.get_amount(), item.get_name(), price_per=item.get_price()/100, price_total=item.get_total_price()/100))
        print("\n1. Name")
        print("2. Amount")
        print("3. Price")
        print("\n4. Done")
        ans = input("\n> ")
        if ans == "1" or ans.lower() == "name":
            item.set_name(input("\nInput new name: \n\n> "))
            self.edit_item(item)
        elif ans == "2" or ans.lower() == "amount":
            item.set_amount(self.validate_num(
                input("\nInput new amount: \n\n> ")))
            self.edit_item(item)
        elif ans == "3" or ans.lower() == "price":
            item.set_price(self.validate_price(
                input("\nInput new price: \n\n> ")))
            self.edit_item(item)
