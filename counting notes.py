Amount= int(input("Please enter Amount for withdraw: "))
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10
print("the number of 100 notes : ", note_1)
print("the number of 50 notes : ", note_2)
print("the number of 10 notes : ", note_3) 