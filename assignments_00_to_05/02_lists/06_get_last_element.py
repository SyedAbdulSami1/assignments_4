#Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

def get_last_element(list):
    """Prints the last element in the list lst."""
    print(f"your list is: {list}")
    print(f"The last element in the list is: {list[-1]}")  # Using negative indexing to get the last element
    return list[-1]  # Returning the last element for further use

def getting_list():
    list = []
    element : str= input("Please enter an element of the list or press enter to stop: ")

    while element != "":
        list.append(element)
        element = input("Please enter an element of the list or press enter to stop: ")
    return list
def main():
    """Main function to execute the program."""
    list = getting_list()
    get_last_element(list)

if __name__ == "__main__":
    main()