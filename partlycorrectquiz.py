def ask(question):
    print(question)
    return input("Enter your answer: ")

def prompt():
    print("Welcome to a simple quiz!!")
    print("1. Anime")
    print("2. Graphic novels")
    print("3. Chemistry")
    return input("Enter your choice 0/1/2/3: ")

choice = prompt()
while (choice != '0'):
    if choice == '1':
        answer = ask("Who is the strongest saiyan alive?")
        if answer == "Goku":
            print("Correct answer")
        elif answer == "Vegeta":
            print("Close, but no cigar")
        else:
            print("Wrong. Get lost")
    elif choice == '2':
        answer = ask("Who is the alternate persona of Bruce Wayne?")
        if answer == "Batman":
            print("Correct answer")
        elif answer == "Superman":
            print("Absolutely wrong")
        else:
            print("Get lost")
    elif choice == '3':
        answer = ask("According to Huckel, what is the nature of benzene?")
        if answer == "Aromatic":
            print("Correct answer")
        else:
            print("Incorrect answer")
    else:
        print("Invalid input")
    print ()
    choice = prompt()

