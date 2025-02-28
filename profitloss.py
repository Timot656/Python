actual_cost = float(input("Enter actual cost: "))
sale_amount = float(input("Enter sale amount "))
if sale_amount > actual_cost:
    profit = sale_amount - actual_cost
    print("Profit: ", profit)
else:
    print("No profit")