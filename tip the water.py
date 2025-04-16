def total_calc(Bill_amount,tip_perc):
    total = Bill_amount *(1 + 0.01 * tip_perc)
    total = round(total,2)
    print(f"Please pay $(total)")
total_calc(150,20)