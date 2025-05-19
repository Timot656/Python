from collections import Counter
test_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
value_to_check = 1
frequency = Counter(test_dict.values())[value_to_check]
print(f"The frequency of {value_to_check} is {frequency}.")