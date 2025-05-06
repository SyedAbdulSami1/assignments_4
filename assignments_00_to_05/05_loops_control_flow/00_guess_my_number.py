"""Guess My Number: I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high"""
import random

def main ():
    secret_number = random.randint(0,99)
    print("I am thinking of a number between 0 and 99..")
    

    guess = int(input("Enter a guess:"))
    condition = True
    while condition:
        if guess < secret_number:
            print("Your guess is too Low")
        elif guess > secret_number:
            print("Your guess is too High")
        else:
            print("Congratulation you guessed it correct ")
            condition=(guess == secret_number)
            break
        
        print()
        
        suggestion = random.randint(4, 10)
        print(f"Please try between {secret_number-suggestion} and {secret_number+suggestion}")
        guess = int(input("Enter a new guess:"))

if __name__ == "__main__":
    main()