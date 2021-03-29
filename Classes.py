#Evive Take Home Allen Wang 2021

from collections import Counter

class Order:
    #order class indentifies the type of order and creates the object
    #order class also prints the order 
    def __init__(self, order):
        order.strip()
        menu_order = order.split(' ')
        #Since the format requires the meal type to be first, we check the first argument
        meal_type = menu_order[0].lower()

        #normally I would just raise an exeception here or an error, but the spec sheet says otherwise
        if (len(menu_order) > 1):
            items = menu_order[1].split(',')
        else:
            items = []

        if meal_type == "breakfast":
            self.meal = Breakfast(items)
        elif meal_type == "lunch":
            self.meal = Lunch(items)
        elif meal_type == "dinner":
            self.meal = Dinner(items)
        else:
            #if the meal type is invalid, it will raise Exception
            raise Exception("Sorry that is an unknown meal type.")

    def print(self):
        if self.meal == None:
            raise Exception("Invalid meal")

        self.meal.print();


class Lunch():
    def __init__(self,order):

        #keeping a dict of the menu so that it can be added to for scalability
        self.lunch_menu = {
            1: ("main", "Salad"),
            2: ("side", "Chips"),
            3: ("drink", "Soda") 
        }

        #because of how the error formatting is on the spec sheet, you need to keep track of multiple errors
        self.error_list = []

        #list of main dishes ordered in format of item name
        self.main = []
        #list of side dishes ordered in format of item name
        self.side = []
        #list of drinks ordered in format of item name
        self.drink = []

        for i in range(len(order)):
            if (int(order[i])) not in self.lunch_menu:
                self.error_list.append("Invalid Item " + order[i])
            else: 
                item = self.lunch_menu[int(order[i])]
                if item[0] == "main":
                    self.main.append(item[1])
                elif item[0] == "side":
                    self.side.append(item[1])
                elif item[0] == "drink":
                    self.drink.append(item[1])
        
        #checking the order for errors 
        if (len(self.main) > 1):
            #alternatively you can say "a main dish cannot be ordered more than once, but the spec sheet called for name of item"
            self.error_list.append(self.main[0] + " cannot be ordered more than once")
        if (len(self.main) < 1):
            self.error_list.append("Main is missing")
        if (len(self.side) < 1):
            self.error_list.append("Side is missing")
        if (len(self.drink) > 1):
            self.error_list.append(self.drink[0] + " cannot be ordered more than once")
        if (len(self.drink) < 1):
            self.drink.append("Water")
    
    def print(self):

        #if there were any errors in the order found, print them
        if len(self.error_list) > 0:
            error_message = "Unable to process: "
            print(error_message + (', '.join(self.error_list)))
            return
        
        #printing the correct format of order
        order = self.main[0] + ", "
        if len(self.side) > 1:
            order += self.side[0] + "(" + str(len(self.side)) +"), "
        else:
            order += self.side[0] + ", "
        order += self.drink[0]
        print(order)



class Dinner():
    def __init__(self,order):

        #keeping a dict of the menu so that it can be added to for scalability
        self.lunch_menu = {
            1: ("main", "Steak"),
            2: ("side", "Potatoes"),
            3: ("drink", "Wine"),
            4: ("desert", "Cake") 
        }

        #because of how the error formatting is on the spec sheet, you need to keep track of multiple errors
        self.error_list = []
        #list of main dishes ordered in format of item name
        self.main = []
        #list of side dishes ordered in format of item name
        self.side = []
        #list of drinks ordered in format of item name (water does not go in list, because water is given)
        self.drink = []
        #list of deserts ordered in format of item name
        self.desert = []
        for i in range(len(order)):
            if (int(order[i])) not in self.lunch_menu:
                self.error_list.append("Invalid Item " + order[i])
            else: 
                item = self.lunch_menu[int(order[i])]
                if item[0] == "main":
                    self.main.append(item[1])
                elif item[0] == "side":
                    self.side.append(item[1])
                elif item[0] == "drink":
                    self.drink.append(item[1])
                elif item[0] == "desert":
                    self.desert.append(item[1])
        
        #checking the order for errors 
        if (len(self.main) > 1):
            #alternatively you can say "a main dish cannot be ordered more than once, but the spec sheet called for name of item"
            self.error_list.append(self.main[0] + " cannot be ordered more than once")
        if (len(self.main) < 1):
            self.error_list.append("Main is missing")

        if (len(self.side) > 1):
            self.error_list.append(self.side[0] + " cannot be ordered more than once")
        if (len(self.side) < 1):
            self.error_list.append("Side is missing")

        if (len(self.drink) > 1):
            self.error_list.append(self.drink[0] + " cannot be ordered more than once")
            
        if (len(self.desert) > 1):
            self.error_list.append(self.desert[0] + " cannot be ordered more than once")
        if (len(self.desert) < 1):
            self.error_list.append("Desert is missing")
        
    
    def print(self):

        #if there were any errors in the order found, print them
        if len(self.error_list) > 0:
            error_message = "Unable to process: "
            print(error_message + (', '.join(self.error_list)))
            return
        
        #printing the correct format of order
        order = self.main[0] + ", "
        order += self.side[0] + ", "
        if (len(self.drink) > 0):
            order += self.drink[0] + ", "
        #water is always added
        order += "Water, "
        order += self.desert[0]
        print(order)

class Breakfast():
    def __init__(self,order):

        #keeping a dict of the menu so that it can be added to for scalability
        self.lunch_menu = {
            1: ("main", "Eggs"),
            2: ("side", "Toast"),
            3: ("drink", "Coffee") 
        }

        #because of how the error formatting is on the spec sheet, you need to keep track of multiple errors
        self.error_list = []

        #list of main dishes ordered in format of item name
        self.main = []
        #list of side dishes ordered in format of item name
        self.side = []
        #list of drinks ordered in format of item name
        self.drink = []

        for i in range(len(order)):
            if (int(order[i])) not in self.lunch_menu:
                self.error_list.append("Invalid Item " + order[i])
            else: 
                item = self.lunch_menu[int(order[i])]
                if item[0] == "main":
                    self.main.append(item[1])
                elif item[0] == "side":
                    self.side.append(item[1])
                elif item[0] == "drink":
                    self.drink.append(item[1])
        
        #checking the order for errors 
        if (len(self.main) > 1):
            #alternatively you can say "a main dish cannot be ordered more than once, but the spec sheet called for name of item"
            self.error_list.append(self.main[0] + " cannot be ordered more than once")
        if (len(self.main) < 1):
            self.error_list.append("Main is missing")

        if (len(self.side) > 1):
            self.error_list.append(self.side[0] + " cannot be ordered more than once")
        if (len(self.side) < 1):
            self.error_list.append("Side is missing")
        
        if (len(self.drink) < 1):
            self.drink.append("Water")
    
    def print(self):

        #if there were any errors in the order found, print them
        if len(self.error_list) > 0:
            error_message = "Unable to process: "
            print(error_message + (', '.join(self.error_list)))
            return
        
        #printing the correct format of order
        order = self.main[0] + ", "
        order += self.side[0] + ", "
        if len(self.drink) > 1:
            order += self.drink[0] + "(" + str(len(self.drink)) +")"
        else:
            order += self.drink[0]
        print(order)

