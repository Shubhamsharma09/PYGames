import random as r
num = r.randint(1,100)
guessed = False
guess = input("Guess my number (1-100):")
while not guessed:
    if(int(guess) == num):
        guessed = True
    else:
        print("lower" if int(guess)>num else "higher");
        guess = input("Next guess:")
print("you guessed correctly!")
