# Prove 09/10
import time


items = []
prices = []


d = "-" * 25
pair = "Price\tItem"
clear = chr(27) + "[2J"  

prompt = """
Please select one of the following:
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit\n
"""

print(clear)

response = None

while response != 5:

    response = int(input(prompt))

    
    if response == 1:
        print(clear)
        x = input("What is the new item you'd like to add? ")
        time.sleep(0.25)
        y = float(input(f"What is the price/cost of the {x}: "))
        print(f"{clear}Adding {x.upper()} to your cart\n...Please wait...")
        time.sleep(1.25)
        items.append(x.title())
        prices.append(y)
        print(clear)

    
    elif response == 2:
        print(clear)
        print(pair)
        print(d)

        for price, item in zip(prices, items):
            print(f"{price:.2f}\t{item}")

        input("\n\nPress Enter to continue...")

    
    elif response == 3:
        print(clear)
        print(pair)
        print(d)

        
        for price, item in zip(prices, items):
            print(f"{price:.2f}\t{item}")

        
        delete_item = input(
            "\nType the name of the item would you like to remove? "
        ).title()

        print(clear)
        print("Deleting item\n...Please wait...")
        time.sleep(1.5)
        print(clear)

        
        index_num = items.index(delete_item)

        items.pop(index_num)
        prices.pop(index_num)

        
        print(pair)
        print(d)
        for price, item in zip(prices, items):
            print(f"{price:.2f}\t{item}")

        input("\n\nPress Enter to continue...")
        print(clear)

    
    elif response == 4:
        print(clear)

        
        print(pair)
        print(d)
        for price, item in zip(prices, items):
            print(f"{price:.2f}\t{item}")

        print(f"\nYour total cart value is ${sum(prices):.2f}")

        input("\n\nPress Enter to continue...")
        print(clear)

print(clear)
print("\nThanks for using the cart!\n")