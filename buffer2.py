str1 = input("Please Enter a Sentence: ")
total = 1
for i in range(len(str1)):
    if(str1[1] == ''):
        total = total + 1
print("The total number of words in the sentence is:  ", total)