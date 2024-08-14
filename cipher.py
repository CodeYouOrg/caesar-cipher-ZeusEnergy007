# add your code here
def caesar_cipher(text, shift):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    alphabet += alphabet    # may handle up to 21 shift
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            char = char.lower()
            encrypted_text += alphabet[alphabet.index(char)+shift]          
        else:
            encrypted_text += char
    return encrypted_text

def main():
    plain_sentence = input("Please enter a sentence: ")
    encrypted_sentence = caesar_cipher(plain_sentence, 5)
    print("The encrypted sentence is:", encrypted_sentence)
    

if __name__ == "__main__":
    main()
