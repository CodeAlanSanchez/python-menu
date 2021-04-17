import math
import item

class Menu():

    list_of_items = []
    line = "="*25
    title = ""

    def __init__(self, title = ""):
        self.title = title
    
    def show_menu(self):
        print(self.line)
        print(math.floor(len(self.line)/2-len(self.title)/2)*" "+self.title+"\n")
        print(self.line+"\n")
        print("1. Show List")
        print("2. Add Item")
        print("3. Edit Item\n")
        print("4. Quit")
        ans = self.validate_input(input("\n> "))
        if ans == 1:
            pass
        if ans == 2:
            pass
        if ans == 3:
            pass
        if ans == 4:
            pass
    
    def validate_input(self, ans, option_range):
        try:
            ans = int(ans)
            if option_range and range(option_range)[ans]:
                return ans
        except:
            return self.validate_input("Please input a valid option...\n> ")
