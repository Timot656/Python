my_set = {1,2,3}
print(my_set)
my_set = {1.0, "hello", (1,2,3)}
print(my_set)
my_set = {1,2,3,4,2,3,5}
print(my_set)
my_set = set([1,2,3,2])
print(my_set, "\n")
num_set = set([0,1,3,4,5])
print("Original set: ")
print(num_set)
num_set.pop()
print("After removing the first element from said set: ")
print(num_set, "\n")