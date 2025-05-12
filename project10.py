user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))
odd_squares = []
even_squares = []
for num in numbers:
    square = num ** 2
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)
print("Odd Squares:", odd_squares)
print("Even Squares:", even_squares)