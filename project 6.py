def calculate_due_amount(total_bill, amount_paid):
    return total_bill - amount_paid
def main():
    try:
        total_bill = float(input("Enter the total bill amount: $"))
        amount_paid = float (input("Enter the amount paid by the customer"))
        due_amount = calculate_due_amount(total_bill, amount_paid)
        if due_amount > 0:
            print(f"The due amount is: ${due_amount:.2f}")
        elif due_amount < 0:
            print(f"The customer has overpaid by: ${-due_amount:.2f}")
        else:
            print("The bill is fully paid. No due amount.")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for the amounts.")

if __name__ == "__main__":
    main()
