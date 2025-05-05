"""In this program we show an example of using dictionaries to keep track of information in a phonebook."""

def read_phone_numbers():
    phonebook= {}

    while True:
        name = input("Name:")
        if name == "":
            break
        number = input("Number:")
        phonebook[name]= number
    return phonebook

def print_phonebooe(phonebook):
    
    for number in phonebook:
        print(str(number) + "-> :" + str(phonebook[number]))
    
def lookup_number(phonebook):
    while True:
        name = input("Enter Name to look up:")
        if name == "":
            break
        if name not in phonebook:
            print(name + "is not in the phonebook")
        else:
            print(phonebook[name])

def main():
    phonebook = read_phone_numbers()
    print_phonebooe(phonebook)
    lookup_number(phonebook)

if __name__ == "__main__":
    main()