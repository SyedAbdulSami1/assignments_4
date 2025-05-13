def madlib():
    adj = input("Adjective: ")
    verb1 = input("Verb 1: ")
    verb2 = input("Verb 2: ")
    famous_person = input("Famous Person: ")

    madlib = f"Programming is so {adj}! It makes me want to {verb1} all day. \n" \
             f"When I feel tired, I just {verb2} like {famous_person} and keep going!"
    
    print(madlib)

if __name__ == "__main__":
    madlib()
