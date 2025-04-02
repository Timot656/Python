number = input("Please enter a number: ")

if number.isdigit() or (number.startswith('-') and number[1:].isdigit()):
    # Count the digits, excluding the negative sign if present
    digit_count = len(number) if number[0] != '-' else len(number) - 1
    print(f"The number of digits in the entered number is: {digit_count}")
else:
    print("Invalid input. Please enter a valid number.")