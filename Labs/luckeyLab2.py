''' 
-----------------------------------------------------------------------------
Solution:       
-----------------------------------------------------------------------------
Developer:      
Course:       
Creation Date:  09/12/2025
Last Mod Date:  09/18/2025
E-mail Address: 
-----------------------------------------------------------------------------
Purpose - Human-age in relation to dog-age
-----------------------------------------------------------------------------
Description of input:
age in human years
Description of output:
dog age 
-----------------------------------------------------------------------------
'''

# Prints what the program is used for

print("\n This program calculats a dog's approximate age in dog years based on human years. " )


# Get human-years

human_years = float(input("Enter human years: "))

# if human years is less than "0" prints error message, else it preforms the calculations

if human_years <=0:

    print("\n error message: Can not be negative:")

else:

     if human_years <= 1:

        dog_years = 15 * human_years

     elif human_years <= 2:
    
        dog_years = 15 + 9 * (human_years -  1)

     else:
      
        dog_years = 15 + 9 + 5 * (human_years - 2)

       
# prints dog's age in human years

print(f"human_years: {human_years:.1f}")
print(f"dog_years: {dog_years:.1f}")




    


        





    

  
  
