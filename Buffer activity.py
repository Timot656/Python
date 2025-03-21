text = input("enter a sentence: ")
text = text.split()
bigworlen = 0
for wrd in text:
    wrdlen = len(wrd)
    if wrdlen > bigworlen:
        bigwordlen = wrdlen
print("\nLargest Word")
for wrd in text:
    wrdlen = len(wrd)
    if wrdlen == bigwordlen:
        print(wrd)