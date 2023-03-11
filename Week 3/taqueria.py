def main():
    total = float(0)
    while True:
        try:
            #enables a user to place an order, prompting them for items, one per line
            #Assume that every item on the menu will be titlecased.
            #Treat the user’s input case insensitively.
            item = str.title(input("Item: "))
            
            total += order(item)
            
            #After each inputted item, display the total cost of all items inputted thus far,
            #prefixed with a dollar sign ($) and formatted to two decimal places.
            print(f"${total:.2f}")
            
        #Ignore any input that isn’t an item.    
        except KeyError:
            pass
          
        #until the user inputs control-d
        except EOFError:
            print()
            break



def order(x):
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    cost = menu[x]

    return cost

main()
