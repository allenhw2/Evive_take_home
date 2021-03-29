#Evive Take Home Allen Wang 2021
import Classes

def main():
    selection = input("")
    order = Classes.Order(selection)
    print(order.print())

if __name__ == "__main__":
    main()