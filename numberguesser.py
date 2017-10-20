import random as r

num = r.randint(1,100)
guessed = False
guess = input("Guess my number (1-100):")

while not guessed:
    numberChoosen = int(guess)
    if(numberChoosen == num):
        guessed = True
    else:
        if (numberChoosen > num):
            print("Lower")
        else:
            print("Higher")
        guess = input("Next guess:")

print("you guessed correctly!")
