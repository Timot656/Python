print("Half Pyramid of Stars (*): ")
n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()