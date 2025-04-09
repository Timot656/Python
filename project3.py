def mirrored_right_triangle(n):
    for i in range(1, n + 1):  
        for j in range(n - i):  
            print(" ", end="")
        for k in range(i):
            print("*", end=" ")
        print()  
height = int(input("Enter the height of the mirrored right angle triangle: "))

mirrored_right_triangle(height)