def check_age():
    try:
        age = int(input("Please enter your age: "))
        
        if age < 0 or age > 120:
            print("The age entered is not valid.")
            if age % 2 == 0:
                print("Additionally, the entered value is even.")
            else:
                print("Additionally, the entered value is odd.")
        else:
            print("The age entered is valid.")
    except ValueError:
        print("The input is not a valid number.")
check_age()