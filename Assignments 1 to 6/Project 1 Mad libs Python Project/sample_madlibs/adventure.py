def madlib():
    adj = input("Adjective: ")
    verb1 = input("Verb 1: ")
    verb2 = input("Verb 2: ")
    famous_person = input("Famous Person: ")

    madlib = f"Life is an {adj} adventure! You must {verb1} with courage \n" \
             f"and {verb2} like you're {famous_person} in a movie."
    
    print(madlib)

if __name__ == "__main__":
    madlib()
