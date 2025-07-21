class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
         
        reversed_text = ' '.join(self.text.split()[::-1])
        return reversed_text

if __name__ == "__main__":
    input_text = "Hello world from Python"
    reverser = StringReverser(input_text)
    print("Original:", input_text)
    print("Reversed:", reverser.reverse_words())