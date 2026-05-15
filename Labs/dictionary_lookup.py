def main():
    # two dictionaries
    item_to_price = {
        "apple": 0.99 ,
        "banana": 0.69 ,
        "grapes": 1.15
    }

    item_to_stock = {
        "apple": 10 ,
        "banana": 5 ,
        "grapes": 15
    }
    #pass dictionaries to a function
    inventory_menu(item_to_price, item_to_stock)

def inventory_menu(price_dict, stock_dict):
    print("INVENTORY SYSTEM")
    print("------------------")

    choice = input("(L)ookup, (A)dd item, (U)pdate, (P)rint all, (Q)uit: ")
    while choice.lower() != "q":
        # ----------------------Lookup---------------------------------------------
        if choice.lower() == "l":
            item = input("Enter item to lookup: ")
            try:
                price = price_dict[item]
                stock = stock_dict[item]
                print(f"{item} cost ${price:.2f} and we have {stock} in stock.\n")
            except KeyError:
                print("That item is not in the system.\n")
        #--------------------------ADDITEM-----------------------------------------
        elif choice.lower()== "a":
            item = input("Enter new item name: ")

            if item in price_dict:
                print("That item already exists.\n ")
            else:
                price = float(input("Enter price: "))
                stock = int(input("Enter stock quanity: "))

                price_dict[item]= price # adds to dictionary 1
                stock_dict[item] = stock #adds to dictionary 2
                print(f"Added {item} with price ${price:.2f}, and stock {stock}.\n")
        #----------------------------UPDATE ITEM------------------------------
        elif choice.lower()== "u":
            item = input("Enter item to update: ")
            # updates item
            try:
                old_price = price_dict[item]
                old_stock = stock_dict[item]
                print(f"Current price: ${old_price:.2f}, stock {old_stock}")

                new_price = float(input("Enter new price: "))
                new_stock = int(input("Enter new stock amount: "))

                price_dict[item] = new_price
                stock_dict[item] = new_stock

                print(f"Updated {item} ${new_price:.2f}, stock {new_stock}.\n")
            except KeyError:
                print("That item does not exist.\n")
        # ---------------------------PRINT ALL------------------------------
        elif choice.lower() == "p":
            print("\nINVENTORY LIST")
            for item in price_dict:
                print(f"{item} - ${price_dict[item]:.2f},stock {stock_dict[item]}")
                print()
        else:
                print("Invalid option.\n")
        choice = input("(L)ookup, (A)dd item, (U)pdate, (P)rint all, (Q)uit: \n")
        print("Done with inventory.\n")
main()
