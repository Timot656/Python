word = (input("Enter in your word: "))
input = word 
if word.isalpha():
    print(f"'{word}' consists entirely of alphabetic characters.")
else:
    print(f"'{word}' contains non-alphabetic characters.")