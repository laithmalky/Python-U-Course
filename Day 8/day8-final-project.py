from art import logo


letters = []

for i in range(ord('a'), ord('z')+1):
    letters.append(chr(i))



'''
type_of_encode = input('Type "encode" to encrypt, type "decode" to decrypt:\n').lower()

o_text = input('Type your message:\n').lower()

o_shift = int(input('Type the shift number:\n'))
'''



'''
def caesar(text, shift, type_of):
    if type_of == 'encode':
        encrypt(en_text = text, en_shift = shift)
    elif type_of == 'decode':
        decrypt(de_text = text, de_shift = shift)
    else:
        print('Invalid input')

'''
def caesar(text, shift, type_of):
    encrypted_text = ''
    for letter in text:
        if letter in letters:
            if type_of == 'encode':
                shifted_position = letters.index(letter) + shift
            elif type_of == 'decode':
                shifted_position = letters.index(letter) - shift
            else:
                print('Invalid input')

            shifted_position %= len(letters) 
            encrypted_text += letters[shifted_position]
        else:
            encrypted_text += letter
    print(f'The {type_of}d text is: {encrypted_text}')
    
        


''' ############### 1st way to encrypt and decrypt #################
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
'''
    

'''  ############### 2nd way to encrypt and decrypt #################
def encrypt(en_text, en_shift):
    encrypted_text = ''
    for letter in en_text:
        if letter in letters:
            shifted_position = letters.index(letter) + en_shift
            shifted_position %= len(letters) 
            encrypted_text += letters[shifted_position]
        else:
            encrypted_text += letter
    print(f'The encoded text is: {encrypted_text}')
'''


''' ############### 1st way to decrypt #################
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

'''

''' ############### 2nd way to decrypt #################
def decrypt(de_text, de_shift):
    decrypted_text = ''
    for letter in de_text:
        if letter in letters:
            shifted_position = letters.index(letter) - de_shift
            shifted_position %= len(letters) 
            decrypted_text += letters[shifted_position]
        else:
            decrypted_text += letter
    print(f'The decoded text is: {decrypted_text}')

'''



# encrypt(text, shift) if type_of_encode == 'encode' else decrypt(text, shift)

keep_going = 'yes'
while keep_going == 'yes':
    type_of_encode = input('Type "encode" to encrypt, type "decode" to decrypt:\n').lower()
    o_text = input('Type your message:\n').lower()
    o_shift = int(input('Type the shift number:\n'))
    caesar(text = o_text, shift = o_shift, type_of = type_of_encode)
    keep_going = input('Type "yes" if you want to go again. Otherwise type "no".\n').lower()
    if keep_going == 'no':
        print('Goodbye')