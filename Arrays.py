import array as arr
array_num = arr.array('i',[1,3,5,3,7,9,3])
print("Original array: "+str(array_num))
print("Number of occurences of the number 3 in rhe said array :" + str(array_num.count(3)))
array_num.reverse()
print("Reverse the order of the Items: ")
print(str(array_num))


