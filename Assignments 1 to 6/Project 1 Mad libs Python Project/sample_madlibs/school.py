def madlib():
    adj = input("Adjective: ")
    verb1 = input("Verb 1: ")
    verb2 = input("Verb 2: ")
    famous_person = input("Famous Person: ")

    madlib = f"School can be {adj}, but if you {verb1} daily and \n" \
             f"{verb2} like {famous_person}, you’ll enjoy learning!"
    
    print(madlib)

if __name__ == "__main__":
    madlib()
