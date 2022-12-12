alphabets = "abcdefghijklmnopqrstuvwxyz"
def caesar_rot13(plaintext):
    ciphertext = []
    for alpha in plaintext:
        if alpha!=' ':
            ciphertextindex = (alphabets.find(alpha)+13)%26
            ciphertext.append(alphabets[ciphertextindex])
        else:
            ciphertext.append(' ')
    return "".join(ciphertext)

def main():
    print("Enter text to encrypt/decrypt:")
    myinput = input("Enter:")
    print("The caesar cipher of rot13 applied to text becomes :"+caesar_rot13(myinput))

main()