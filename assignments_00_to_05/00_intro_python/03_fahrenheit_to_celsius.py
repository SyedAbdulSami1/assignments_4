"""Fahrenheit to Celsius Converter:
This program converts a temperature from Fahrenheit to Celsius."""
def get_tem (prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("This program converts Fahrenheit to Celsius.")
    fahrenheit_temp = get_tem("Enter Temperature in Fahrenheit: ")
    celsius_temp = (fahrenheit_temp - 32) * 5.0/9.0
    # ANSI escape codes for italic and bold
    italic = "\033[3m"
    bold = "\033[1m"
    reset = "\033[0m"
    formated_fahrenheit = f"{italic}{bold}{celsius_temp:.2F}{reset}"
    print(f"{fahrenheit_temp} Fahrenheit is equal to {formated_fahrenheit:} Celsius.")

if __name__ == '__main__':
    main()