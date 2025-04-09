"""Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works."""
import random

num_sides=6
def roll_dice():
    """Simulates rolling two dice and prints their total"""
    dice1:int=random.randint(1, num_sides)
    dice2:int=random.randint(1, num_sides)
    total:int=dice1 + dice2
    print(f"Total of rolling two dice: {dice1} + {dice2} = {total}")

def main():
    dice1:int=10
    print(f"dice1 in main() start as: " + str(dice1))
    roll_dice()
    roll_dice()
    roll_dice()
    print(f"dice1 in main() is: " + str(dice1))

if __name__ == "__main__":
    main()