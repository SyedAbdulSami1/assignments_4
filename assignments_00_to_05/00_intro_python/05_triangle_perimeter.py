"""Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).
Here's a sample run of the program (user input is in bold italics):
What is the length of side 1? 3
What is the length of side 2? 4
What is the length of side 3? 5.5
The perimeter of the triangle is 12.5"""
def get_side_length(prompt):
    while True:
        try:
            return float(input(prompt))  
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    side_1 :float = get_side_length("What is the length of side 1?")
    side_2 :float = get_side_length("What is the length of side 2?")
    side_3 :float = get_side_length("What is the length of side 3?")
    perimeter = side_1 + side_2 + side_3
    print(f"The perimeter of the triangle is {perimeter}")

if __name__ == "__main__":
    main()
