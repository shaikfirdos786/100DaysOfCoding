import random
from replit import clear
from art import logo
from art import logo1
from art import logo2
from art import logo3

while input("Do you want to play the game? ") == 'yes':
    clear()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    my_guess = random.randint(1, 100)
    

    difficulty = input("Choose a difficulty level. 'easy' or 'hard' ? ")

    if difficulty.lower() == 'easy':
        attempts = 10
        print(f"You have {attempts} attempts remainig to guess the number.")
    elif difficulty.lower() == 'hard':
        attempts = 5
        print(f"You have {attempts} attempts remainig to guess the number.")

    while attempts != 0:
        guess = int(input("Make a guess. "))
        if guess == my_guess:
            print()
            print("Congratulations")
            print(f"You got it!. The answer was {my_guess}.")
            print(logo1)
            print()
            break

        elif guess > my_guess:
            attempts -= 1
            if attempts == 0:
                print()
                print("Too high!")
                print("You loose!, you are out of guesses. ")
                print(logo3)
                print()
                break

            print()
            print("Too high!")
            print("Guess again.")
            print(f"You have {attempts} attempts remainig to guess the number.")
            print(logo2)
            print()

        elif guess < my_guess:
            attempts -= 1
            if attempts == 0:
                print()
                print("Too low!")
                print("You loose!, you are out of guesses. ")
                print(logo3)
                print()
                break

            print()
            print("Too low!")
            print("Guess again.")
            print(f"You have {attempts} attempts remainig to guess the number.")
            print(logo2)
            print()
