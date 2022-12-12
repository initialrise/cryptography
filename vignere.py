def encrypt(plain_text, key):
    cipher_text = ''
    for i in range(len(plain_text)):
        plain_text_char_ascii = ord(plain_text[i]) - 65
        key_char_ascii = ord(key[i % len(key)]) - 65
        cipher_char_ascii = (plain_text_char_ascii + key_char_ascii) % 26;

        cipher_text += chr(cipher_char_ascii + 65)
    return cipher_text


def decrypt(cipher_text, key):
    plain_text = ''
    for i in range(len(cipher_text)):
        cipher_char_ascii = ord(cipher_text[i]) - 65
        key_char_ascii = ord(key[i % len(key)]) - 65
        plain_text_char_ascii = (cipher_char_ascii - key_char_ascii) % 26;

        plain_text += chr(plain_text_char_ascii + 65)
    return plain_text


def main():
    inp_text = input("Enter input text:(UPPER TEXT):") 
    key = 'RABINDRA'
    choice = int(input("Enter 1 for encryption and 2 for decryption:"))
    if choice==1:
        print("The ciphertext is: "+encrypt(inp_text,key))
    elif choice==2:
        print("The ciphertext is: "+decrypt(inp_text,key))

main()
