import random

number = random.randint(1, 100)

while True:
    guess = input("Guess the number from 1 to 100")
    if guess.isnumeric():
        guess = int(guess)
        if(guess > number):
            print("Your guess was higher than the number")
            continue
        elif(guess < number):
            print("Your guess was lower than the number")
            continue
        else:
            print("You guessed the number correctly!")
            break
    else:
        print("Please enter a valid number")
        continue