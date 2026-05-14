''' 
-----------------------------------------------------------------------------
Solution:      luckeyLab6.py 
-----------------------------------------------------------------------------
Developer:      Victoria Luckey
Course:         Intro to Programming & Logic - CITC-1301
Creation Date:  10/10/2025
Last Mod Date:  10/14/2025
E-mail Address: vlluckey@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - To guess a random number within three tries to be accepted
-----------------------------------------------------------------------------
Description of input: get a user to guess a number
Description of output:
Try again, Congratuatlions You been accepted, or You are not ready 
-----------------------------------------------------------------------------
'''

#imports random number 
import random

def main():
    secret = random.randint(1, 20)
    attempts = 0
    guess = 0 

   # keeps running until the correct number is guessed
    while guess != secret:
        # asks the user to guess a number 1 - 20
        guess = int(input("Guess a number between 1 - 20 "))
        # keeps track of attempts
        attempts += 1
        # if guess is too low guess agian
        if guess < secret:
            print("Too Low, Guess again ")
         # if guess is too high guess again
        elif guess > secret:
            print("Too High, Guess again ")
        else:
            # if user guesses the correct number in 3 or less trys prints "Congrats"
            if attempts <= 3:
                print("Congratulations, been accepted to the Jedi Council you have!")
            # if user guesses the number but takes more than 3 trys prints "Not ready"
            else:
                print("Ready for the Jedi Council you are not. Weak with the force you are!")
main()



     

