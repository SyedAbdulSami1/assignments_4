def madlib():
    adj = input("Adjective: ")
    verb1 = input("Verb 1: ")
    verb2 = input("Verb 2: ")
    famous_person = input("Famous Person: ")

    madlib = f"Success is {adj}. First, you must {verb1}, and never stop. \n" \
             f"Just {verb2} like {famous_person}, and reach your dreams!"
    
    print(madlib)

if __name__ == "__main__":
    madlib()
