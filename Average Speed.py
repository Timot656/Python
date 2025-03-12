a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
c = int(input("Enter c value: "))
avg = (a+b+c)/3
print("Average of a,b,c is: ", avg)
if avg > a and avg > b and avg > c:
    print("%d is higher than %d, %d "%(avg,a,b))
elif avg > a and avg > b:
    print("%d is higher than %d, %d "%(avg,a,b))
elif avg > a and avg > c:
    print("%d is higher than %d, %d "%(avg,a,c))
elif avg > b and avg > c:
    print("%d is higher than %d, %d "%(avg,b,c))
elif avg > a:
    print("%d is  just higher than %d, %d "%(avg,a))
elif avg > b:
    print("%d is just higher than %d, %d "%(avg,b))
elif avg > c:
    print("%d is just higher than %d, %d "%(avg,c))
else:
    print("Invalid input")