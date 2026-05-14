''' 
-----------------------------------------------------------------------------
Solution:       
-----------------------------------------------------------------------------
Developer:      
Course:         
Creation Date:  09/19/2025
Last Mod Date:  09/25/2025
E-mail Address: 
-----------------------------------------------------------------------------
Purpose - To double your investment in stockmarket every year
-----------------------------------------------------------------------------
Description of input:
get number of years
Description of output:
table showing the amount of the account for each year

-----------------------------------------------------------------------------
'''
# get the amount of years invested
years = int (float(input("How many years have you invested? ")))

# Prints the table
print('Years\tTotal')
print('--------------')

# amount starting with for investment
STARTUP = 100.00
total = 0.00

# The range the table starts and ends based off of users input
for year in range(years + 1):
  
  # prints the amount of investment and doubles it every year
  # calculates the total of the account 

   print(year, f"\t${STARTUP:.2f}")
   total  += STARTUP
   STARTUP *= 2

# prints the total value of the account 
print(f"The total value of your accout after {years} years is ${STARTUP/2:.2f}")



