def main():
    animal_name = str(input("What's your favorite animal? ")).upper()
    # ANSI escape codes for italic and bold
    italic = "\033[3m"
    bold = "\033[1m"
    reset = "\033[0m"
    formated_animal = f"{italic}{bold}{animal_name}{reset}"

    print(f"My favorite animal is also {formated_animal}!")

if __name__ == "__main__":
    main()