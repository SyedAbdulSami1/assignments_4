def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
def main():
    num: float = get_number("Type a number to see its square:")
    print(str(num) + " squared is " + str(num ** 2)) 

if __name__ == '__main__':
    main()
