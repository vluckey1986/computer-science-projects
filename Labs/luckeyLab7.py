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
Purpose - character.txt file and writes to it
-----------------------------------------------------------------------------
Description of input: no input required

Description of output: list of characters and assigns a random number

----------------------------------------------------------------------------
'''

# This program creates a character.txt file and assigns a random number
import random

def main():

    try: 
        # Opens file
        file = open('character.txt', 'w') 
      
      # writes the words "strength, constitution, intelligence, wisdom, dexderity and charisma" to the file
      # creates random number for each word
        file.write(f'Strength {random.randint(1, 18)}\n')
        file.write(f'Constituion {random.randint(1, 18)}\n')
        file.write(f'Intelligence {random.randint(1,18)}\n')
        file.write(f'Wisdom {random.randint(1, 18)}\n')
        file.write(f'Dexderity {random.randint(1, 18)}\n')
        file.write(f'Chrisma {random.randint(1, 18)}\n')
        
        # closes the file
        file.close()
    # error message
    except IOError:
      print("Error has occured")

main()
