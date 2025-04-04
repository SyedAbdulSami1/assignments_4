"""
Add 2 Numbers:
This function sum two numbers.
"""
def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
def main():
    print("This program adds two numbers.")
    first_num = get_number("Enter First Number: ")
    second_num = get_number("Enter Second Number: ")
    print(f"The sum of {first_num} and {second_num} is {first_num + second_num}.")
if __name__ == '__main__':
    main()