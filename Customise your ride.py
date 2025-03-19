print("Select your ride: ")
print("!. bike")
print("2. car")
choice = int(input("enter your choice: "))
if(choice == 1):
    print("what type of bike? ")
    print("1. Scooty\n")
    print("2. Scooter\n")
    choice2 = int(input("Enter your choices: "))
    if choice2 == 1:
       print("You have selected Scooty")
    else:
       print("You have selected Scooter")
elif (choice == 2):

    print("What type of car? ")
    print("1. SUV\n")
    print("2. Sedan\n")
    choice3 = int(input("Enter your choice3: "))
    if choice3 == 1:
       print("You have selected SUV")
    else:
       print("You hve selected Sedan")
else:
    print("Wrong choice: ")


