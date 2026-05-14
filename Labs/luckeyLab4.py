''' 
-----------------------------------------------------------------------------
Solution:       
-----------------------------------------------------------------------------
Developer:       
Course:         
Creation Date:  09/27/20025
Last Mod Date:  10/02/2025
E-mail Address: 
-----------------------------------------------------------------------------
Purpose - To get a postivie number and have a sentinel to quit and sum all numbers
-----------------------------------------------------------------------------
Description of input:
Get a positive number from the user
Description of output:
Sum of the numbers entered excluding the sentinel
-----------------------------------------------------------------------------
'''

# initialize number
number = 0

# initialize sentinel to end program
sentinel = 67 

# initialize sum to 0
sum = 0

# While loop asks user to enter positive number until sentienl is entered
while True:
    number = int(input(f"Enter a positive number ({sentinel} to quit): "))
    # If sentinel is entered program ends
    if number == sentinel:
        break
    # Else if the number is negative ask user to re-enter positive number
    elif number < 0:
     print("Re-enter a positive number." )
     continue
    # Adds of the positive numbers enter excluding the sentinel
    else:
     sum += number

  # Prints the sum of the positive numbers enterend excluding the sentinel
print("The sum of the numbers entered is:", sum)

 
   

  
