
print('''
    Hello user! You must enter kilometres and the program will automatically convert kilometres to miles for you.
    Enjoy!''')

while True:

    try:
        ask = int(input("Enter kilometres: "))
    except ValueError:
        print("You can only enter a number.")
        cont = input("Continue? [y/n] ")
        if cont.lower() == "n":
            print("Bye")
            break
        if cont.lower() == "y":
            continue
        else:
            print("You have entered invalid symbol. The program will stop runing. Goodbye")
            break

    miles = 0.621371192
    converter = ask * miles
    print(f"Your entered distance is equal to  %s  miles" %(converter))

    cont = input("Continue? [y/n] ")
    if cont.lower() == "n":
        print("Bye")
        break
    if cont.lower() == "y":
        continue
    else:
        print("You have entered invalid symbol. The program will stop runing. Goodbye")
        break
