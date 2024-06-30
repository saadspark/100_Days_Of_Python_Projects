from alphabet import alphabet
from alphabet import logo
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def decrypt(text,shift) :
    decrypted_text = ''
    for i in text :
        index = alphabet.index(i)
        decrypted_text += alphabet[index-shift]
    print(decrypted_text)
    
def encrypt(text,shift,direction) :
    entered_text = ''
    for i in text :
        index = alphabet.index(i)
        if direction == 'decode' :
          entered_text += alphabet[index-shift]
        else :
            entered_text += alphabet[index+shift]
    print(f'Your {direction} Text is : {entered_text}')


if direction == 'encode'or direction == 'decode' :
    encrypt(text,shift,direction)
else :
    print("You entered an invalid direction. Please type 'encode' or 'decode'.")