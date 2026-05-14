import random
def main ():
    try:
        file = open("random.txt", 'w')
        file.write(f'RANDOM {random.randint(1 , 18)}')
        file.close
    except IOError:
        print("Error has occured")
main ()
