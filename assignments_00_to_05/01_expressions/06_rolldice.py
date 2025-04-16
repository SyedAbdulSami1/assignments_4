"""Simulate rolling two dice, and prints results of each roll as well as the total."""
import random

num_sides : int = 6

def roll_dice():
    dice_1 : int = random.randint(1, num_sides)
    dice_2 : int = random.randint(1, num_sides)
    total : int = dice_1 + dice_2

    # Print out the results
    print(f"Dice have {num_sides} sides each.")
    print(f"First die: {dice_1}")
    print(f"Second die: {dice_2}")
    print(f"Total of two dice: {total}")

if __name__ == "__main__":
    roll_dice()