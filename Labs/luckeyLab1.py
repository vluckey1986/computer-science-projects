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
Purpose - Get character information from user and calculate
-----------------------------------------------------------------------------
Description of input:
get character name, level, hitpoints, amount of gold
Description of output:
user input of character information and amount of rations
-----------------------------------------------------------------------------
'''
# Get character information

name = input("What is your Character's name? ")

level = int(input("What is your level? "))

hitpoints = int(input("How many hitpoints do you have? "))

gold = int(input("How much gold do you have? "))


# Cost of rations

rations = 5


# Calculates rations they can purchase

rations =  float(gold // rations)


# Prints user's answers and the amount of rations that they can purchase

print("\n Character information you entered: ")
print('name:', name.capitalize(),)
print('level:', level)
print('hitpoints:', hitpoints)
print('gold:', gold)
print('The number of rations you can purchase is', rations)







