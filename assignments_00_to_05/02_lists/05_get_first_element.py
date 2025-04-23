"""Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.
"""

def get_first_element(list):
    print(f"your list is: {list}")
    print(f"The first element in the list is: {list[0]}")

def macking_list():
    list = []
    element = input("Pleas enter an element of the list or press enter to stop: ")

    while element !="":
        list.append(element)
        element = input("Pleas enter an element of the list or press enter to stop:")
    return list
    
def main():
    list = macking_list()
    get_first_element(list)

if __name__ == "__main__":
    main()