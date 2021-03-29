#Evive Take Home Allen Wang 2021
import unittest as test
from unittest.mock import patch, call
import Classes

from io import StringIO

class TestMenu(test.TestCase):

    def test_incorrect_meal_type(self):
        #tests whether or not an error is raised when you input invalid meal type
        order = "brunch 1,2,3"
        try:
            menu = Classes.Order(order)
            self.assertFalse
        except:
            self.assertTrue
    
    def test_empty_meal_type(self):
        #tests whether or not an error is raised when you input invalid meal type
        order = ""
        try:
            menu = Classes.Order(order)
            self.assertFalse
        except:
            self.assertTrue
    def test_incorrect_format(self):
        #tests whether or not the code can handle incorrect ordering format
        order = "breakfast 1, 2, 3"
        try:
            menu = Classes.Order(order)
            self.assertFalse
        except:
            self.assertTrue
        

    def test_breakfast_standard(self):
        #this test also covers whether or not the type needs to be capitalized
        order = "breakfast 1,2,3"
        menu = Classes.Order(order);
        self.assertEqual(menu.print(),"Eggs, Toast, Coffee")
    
    def test_breakfast_missing_items(self):
        #tests when you have missing items (Main, side, Main & side, drink)
        order_missing_main = "breakfast 2,3"
        order_missing_side = "breakfast 1,3"
        order_missing_main_side = "breakfast 3"
        order_missing_drink = "breakfast 1,2"

        menu = Classes.Order(order_missing_main)
        self.assertEqual(menu.print(),"Unable to process: Main is missing")

        menu = Classes.Order(order_missing_side)
        self.assertEqual(menu.print(),"Unable to process: Side is missing")

        # the code stacks error messages
        menu = Classes.Order(order_missing_main_side)
        self.assertEqual(menu.print(),"Unable to process: Main is missing, Side is missing")

        menu = Classes.Order(order_missing_drink)
        self.assertEqual(menu.print(),"Eggs, Toast, Water")
    
    def test_breakfast_multiple_items(self):
        #test the ordering of multiple items
        order_multiple_main = "breakfast 1,1,2,3"
        order_multiple_side = "breakfast 1,2,2,3"
        order_multiple_drink = "breakfast 1,2,3,3,3"

        menu = Classes.Order(order_multiple_main)
        self.assertEqual(menu.print(),"Unable to process: Eggs cannot be ordered more than once")

        menu = Classes.Order(order_multiple_side)
        self.assertEqual(menu.print(),"Unable to process: Toast cannot be ordered more than once")

        menu = Classes.Order(order_multiple_drink)
        self.assertEqual(menu.print(),"Eggs, Toast, Coffee(3)")
    

    #Lunch Tests
    def test_lunch_standard(self):
        #this test also covers whether or not the type needs to be capitalized
        order = "lunch 1,2,3"
        menu = Classes.Order(order);
        self.assertEqual(menu.print(),"Salad, Chips, Soda")
    
    def test_lunch_missing_items(self):
        #tests when you have missing items (Main, side, Main & side, drink)
        order_missing_main = "lunch 2,3"
        order_missing_side = "lunch 1,3"
        order_missing_main_side = "lunch 3"
        order_missing_drink = "lunch 1,2"

        menu = Classes.Order(order_missing_main)
        self.assertEqual(menu.print(),"Unable to process: Main is missing")

        menu = Classes.Order(order_missing_side)
        self.assertEqual(menu.print(),"Unable to process: Side is missing")

        menu = Classes.Order(order_missing_main_side)
        self.assertEqual(menu.print(),"Unable to process: Main is missing, Side is missing")

        menu = Classes.Order(order_missing_drink)
        self.assertEqual(menu.print(),"Salad, Chips, Water")
    
    def test_lunch_multiple_items(self):
        #test the ordering of multiple items
        order_multiple_main = "lunch 1,1,2,3"
        order_multiple_side = "lunch 1,2,2,3"
        order_multiple_drink = "lunch 1,2,3,3,3"

        menu = Classes.Order(order_multiple_main)
        self.assertEqual(menu.print(),"Unable to process: Salad cannot be ordered more than once")

        menu = Classes.Order(order_multiple_side)
        self.assertEqual(menu.print(),"Salad, Chips(2), Soda")

        menu = Classes.Order(order_multiple_drink)
        self.assertEqual(menu.print(),"Unable to process: Soda cannot be ordered more than once")

    
    #Dinner Tests
    def test_dinner_standard(self):
        #this test also covers whether or not the type needs to be capitalized
        order = "dinner 1,2,3,4"
        menu = Classes.Order(order);
        self.assertEqual(menu.print(),"Steak, Potatoes, Wine, Water, Cake")
    
    def test_dinner_missing_items(self):
        #tests when you have missing items (Main, side, Main & side, drink)
        order_missing_main = "dinner 2,3,4"
        order_missing_side = "dinner 1,3,4"
        order_missing_desert = "dinner 1,2,3"
        order_missing_main_side_desert = "dinner 3"
        order_missing_drink = "dinner 1,2,4"

        menu = Classes.Order(order_missing_main)
        self.assertEqual(menu.print(),"Unable to process: Main is missing")

        menu = Classes.Order(order_missing_side)
        self.assertEqual(menu.print(),"Unable to process: Side is missing")

        menu = Classes.Order(order_missing_desert)
        self.assertEqual(menu.print(),"Unable to process: Desert is missing")

        menu = Classes.Order(order_missing_main_side_desert)
        self.assertEqual(menu.print(),"Unable to process: Main is missing, Side is missing, Desert is missing")

        menu = Classes.Order(order_missing_drink)
        self.assertEqual(menu.print(),"Steak, Potatoes, Water, Cake")
    
    def test_dinner_multiple_items(self):
        #test the ordering of multiple items
        order_multiple_main = "dinner 1,1,2,3,4"
        order_multiple_side = "dinner 1,2,2,3,4"
        order_multiple_desert = "dinner 1,2,3,4,4"
        order_multiple_drink = "dinner 1,2,3,3,3,4"

        menu = Classes.Order(order_multiple_main)
        self.assertEqual(menu.print(),"Unable to process: Steak cannot be ordered more than once")

        menu = Classes.Order(order_multiple_side)
        self.assertEqual(menu.print(),"Unable to process: Potatoes cannot be ordered more than once")

        menu = Classes.Order(order_multiple_desert)
        self.assertEqual(menu.print(),"Unable to process: Cake cannot be ordered more than once")

        menu = Classes.Order(order_multiple_drink)
        self.assertEqual(menu.print(),"Unable to process: Wine cannot be ordered more than once")

if __name__ == '__main__':
    test.main()