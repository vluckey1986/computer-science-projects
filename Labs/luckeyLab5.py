''' 
-----------------------------------------------------------------------------
Solution:       luckeyLab5.py
-----------------------------------------------------------------------------
Developer:      Victoria Luckey
Course:         Intro to Programming & Logic - CITC-1301
Creation Date:  10/01/2025
Last Mod Date:  10/07/2025
E-mail Address: vluckey@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - Get human age from user
-----------------------------------------------------------------------------
Description of input:
input age in human years and ask the user if they want to calculate another dogs age
Description of output:
outputs dog age in human years
-----------------------------------------------------------------------------
'''


#Constants
FIRST_YEAR_EQUIV = 15
SECOND_YEAR_EQUIV = 9
THREE_PLUS_YEARS_MULTIPLIER = 5


def main(): 
    # Output program's purpose
     print("This program calculate's a dog's approximate age in \"dog years\" based on human years.\n")

    # Get human years from user
     humanYears = float(input("Dog's age in human years? "))
    
     while humanYears < 0:
        print("\nHuman age must be a positive number.")
        humanYears = float(input("Dog's age in human years? "))
     
     else:
        # call getDogYears(humanYears)
        dogYears = getDogYears(humanYears)
        print("\nA dog with a human age of", format(humanYears, ",.1f"), "years is", 
            format(dogYears, ",.1f"), "in dog years.")
        
        # ask if the user wants to calculate anoter dog's age
        again = input("Would you like to calculate another dog's age (y,n): ")
     while again == "y":
         main()
         break
    
         
        # Human years to dog years calculation
def getDogYears(humanYears):
        
        
        if humanYears <= 1:
            return FIRST_YEAR_EQUIV * humanYears
        elif humanYears <= 2:
            return FIRST_YEAR_EQUIV + SECOND_YEAR_EQUIV * (humanYears - 1)
        else:
            return FIRST_YEAR_EQUIV + SECOND_YEAR_EQUIV + THREE_PLUS_YEARS_MULTIPLIER * (humanYears - 2)
        # call main 
        # end if

       
    # end if
# end function

# DO NOT MODIFY CODE BELOW THIS LINE
if __name__ == "__main__":
    main()
# end if
