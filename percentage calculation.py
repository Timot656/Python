print("Enter marks Obtained in 4 subjects: ")
math = int(input("Mathematics: "))
phy = int(input("Physics: "))
chem = int(input("Chemistry: "))
comp = int(input("Computer: "))
total = math + phy + chem + comp
print("Total Marks Obtained: ", total)
percentage = (total/400)*100
print(end= "Percentage Mark = ")
print(percentage)