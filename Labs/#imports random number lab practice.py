#imports random number 
import random

def main():
    secret = random.randint(1, 20)
    attempts = 0
    guess = 0

    while guess != secret:
        guess = int(input("Guess a number between 1 - 20 "))

        attempts += 1
        
        if guess < secret:
            print("Too Low, Guess again ")
        elif guess > secret:
            print("Too High, Guess again ")
        else:
            if attempts <= 3:
                print("Congratulations, been accepted to the Jedi Council you have!")
            else:
                print("Ready for the Jedi Council you are not. Weak with the force you are!")
main()

