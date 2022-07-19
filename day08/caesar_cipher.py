alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decript:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number\n"))

def encrypt(text, shift):
    text_len = len(text)
    encrypted_text = []
    encrypted_text[:0]= text
    for i in range (0, text_len):
        for j in range (0, len(alphabet)):
            if alphabet[j] == text[i]:
                if (j+shift) < len(alphabet):
                    encrypted_text[i] = alphabet[j+shift]
                else:
                    encrypted_text[i] = alphabet[j+shift-len(alphabet)]
            else:
                continue
    print(''.join(encrypted_text))


def decrypt(text, shift):
    text_len = len(text)
    decrypted_text = []
    decrypted_text[:0]= text
    for i in range (0, text_len):
        for j in range (0, len(alphabet)):
            if alphabet[j] == text[i]:
                if (j-shift) >= 0:
                    decrypted_text[i] = alphabet[j-shift]
                else:
                    decrypted_text[i] = alphabet[j-shift-1]
            else:
                continue

    print(''.join(decrypted_text))

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Please select the correct option.")
    
