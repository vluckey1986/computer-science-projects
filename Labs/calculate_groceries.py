''' 
-----------------------------------------------------------------------------
Solution:      
-----------------------------------------------------------------------------
Developer:      
Course:         
Creation Date:  
Last Mod Date: 
E-mail Address: 
-----------------------------------------------------------------------------
Purpose - Create a Grocery List and calculates the total, average, highest and lowest
-----------------------------------------------------------------------------
Description of input:
Get the amount spent monthly on groceries
Description of output:
Print the highest and lowest month, the average spent and the yearly cost.
-----------------------------------------------------------------------------
'''
# Imports the module that contains the names of the months
import calendar

# Start of the program
def main ():
    # Prints what the program does
    print("This program calculates the amount spent on groceries and displays the total, average, highest and lowest amount.\n")

    # Creates empty list for amount spent
    grocery_bill = []
    # Gets the name of the month from calendar and skips the first index
    months = calendar.month_name[1: ]

    try:
      # Starts the loop to ask for each month how much was spent
      for month in months:
        # Ask the user how much they spent each month
        spent = float(input(f"Enter how much you spent? {month}:$"))
        # Stores the amount enter 'spent' to the grocery bill list
        grocery_bill.append(spent)

      # Totals the amounts entered 
      total = sum(grocery_bill)
      # Takes the total and divides by the number of entries entered in grocery bill list
      average = total / len(grocery_bill)
      # Gets the highest amount spent
      highest = max(grocery_bill)
      # Gets the index of the highest amount spent
      index_of_highest = grocery_bill.index(highest)
      # Gets the name of the month from the index for the highest amount
      month_of_highest = months[index_of_highest]
      # Gets the lowest amount spent
      lowest = min(grocery_bill)
      # Gets the index of the lowest amount spent
      index_of_lowest = grocery_bill.index(lowest)
      # Gets the name of month from index for lowest amount
      month_of_lowest = months[index_of_lowest]

      # Prints the total of the grocery bill list
      print(f"Total grocery bill: ${total:,.2f}")
      # Prints the average of the grocery bill list
      print(f"Average grocery bill: ${average:,.2f}")
      # Prints the month with the highest amount spent
      print(f"Highest grocery bill {month_of_highest}")
      # Prints the month with the lowest amount spent
      print(f"Lowest grocery bill {month_of_lowest}")

    # If something other than a number is entered, prints error message
    except ValueError:
     print("Invailid Input. Please enter a Number. ")
    
main ()
