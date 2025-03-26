def power(base, exp):
  """
  Calculates the power of a number.

  Args:
    base: The base number.
    exp: The exponent.

  Returns:
    The result of base raised to the power of exp.
  """
  return base ** exp
base = float(input("Enter the base number: "))
exp = int(input("Enter the exponent: "))
result = power(base, exp)
print(f"{base} raised to the power of {exp} is: {result}")