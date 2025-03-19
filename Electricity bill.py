unit = int(input("Please enter number of units you consumed: "))
if (unit < 50):
    amount = unit *2.00
    subcharges = 25
elif (unit <= 100):
    amount = 130 +((unit - 50) *3.25)
    subcharges = 35
elif (unit <= 200):
    amount = 130 + 162.50 ((unit - 100) *5.26)
    subcharges = 45
else:
     amount = 130 + 162.50 + 526 + ((unit - 200) *8.45)
     subcharges = 75 
total = amount + subcharges
print("\n Electricity Bill - %.2f" %total)
