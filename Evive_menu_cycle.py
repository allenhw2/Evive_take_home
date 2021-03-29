#Evive Take Home Allen Wang 2021
import Classes

def main():
    selection = input("Hello and Welcome! \nWhat would you like to order?\n")

    while selection != "nothing":
        order = Classes.Order(selection)
        order.print()
        selection = input("What would you like to order?\nYou can also leave by ordering 'nothing'!\n")
    
    input('Press ENTER to exit')
    print("Alright have a nice day!")

if __name__ == "__main__":
    main()