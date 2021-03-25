import random

def guess(x):
    Random_Number=random.randint(1,x)
    guessed_number=0

    while guessed_number!=Random_Number:
        guessed_number=int(input("Guess the number: "))
        if guessed_number>Random_Number:
            print("Sorry, number too high")
        elif guessed_number<Random_Number:
            print("Sorry, number too low")

    print("congrats nigga. You gots it!")


guess(10)