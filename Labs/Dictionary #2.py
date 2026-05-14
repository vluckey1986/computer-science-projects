def main():
    # creates 2 dictionaries
    item_to_price = {
        "apple": 0.99,
        "banana": 0.69,
        "grapes": 1.15
        }
    
    item_to_stock ={
        "apple": 10,
        "banana": 5,
        "grapes": 15
    }

    #pass dictionaries to function
    shopping(item_to_price, item_to_stock)

def shopping(item_dict, stock_dict):
    item = input("Enter item (or 'done'): ")
    while item.lower():
        try:
            #try to access dictionaries wity key
            price = item_dict[item]
            stock = stock_dict[item]
            print(f"{item} costs ${price:.2f} and we have {stock} in stock")
        except KeyError:
            #runs if item is not in dictionary
            print("Item not found in system.\n")
        item = input("Enter item ()'or done): ")
    print("Done looking up items.\n")
main()