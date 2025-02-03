
letters = []

for i in range(ord('a'), ord('z')+1):
    letters.append(chr(i))

type_of_encode = input('Type "encode" to encrypt, type "decode" to decrypt:\n').lower()

o_text = input('Type your message:\n').lower()

o_shift = int(input('Type the shift number:\n'))

def caesar(text, shift, type_of):
    if type_of == 'encode':
        encrypt(en_text = text, en_shift = shift)
    elif type_of == 'decode':
        decrypt(de_text = text, de_shift = shift)
    else:
        print('Invalid input')


def encrypt(en_text, en_shift):
    encrypted_text = ''
    for letter in en_text:
        if letter in letters:
            position = letters.index(letter)
            new_position = position + en_shift
            if new_position > 25:
                new_position = new_position - 26
            encrypted_text += letters[new_position]
        else:
            encrypted_text += letter
    print(f'The encoded text is: {encrypted_text}')

def decrypt(de_text, de_shift):
    decrypted_text = ''
    for letter in de_text:
        if letter in letters:
            position = letters.index(letter)
            new_position = position - de_shift
            if new_position < 0:
                new_position = new_position + 26
            decrypted_text += letters[new_position]
        else:
            decrypted_text += letter
    print(f'The decoded text is: {decrypted_text}')


# encrypt(text, shift) if type_of_encode == 'encode' else decrypt(text, shift)

caesar(text = o_text, shift = o_shift, type_of = type_of_encode)