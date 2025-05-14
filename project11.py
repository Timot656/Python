from functools import reduce

def calculate_product(numbers):
    return reduce(lambda x, y: x * y, numbers)
numbers = (2, 3, 4)
result = calculate_product(numbers)
print("Product:", result)