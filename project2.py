def decimal_to_binary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary if binary else "0"
decimal_number = 10
binary_number = decimal_to_binary(decimal_number)
print(f"Binary representation of {decimal_number} is {binary_number}")