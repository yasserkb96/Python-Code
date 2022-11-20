print('Caesar Cipher:')
print('(-) for left rotation')
print('key * (-1) for decryption')
print('text needs to be written in upper case letters')

Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

Initial_Text = input('Initial Text : ')
Key = int(input('Key = '))

if Key >= 0:
    Cipher = Alphabet[Key:]+Alphabet[:Key-26]
else:
    Cipher = Alphabet[Key+26:]+Alphabet[:Key]

print(f'Cipher : {Cipher}')

Encrypted_Text = Initial_Text

for j in range(len(Initial_Text)):
    if Initial_Text[j] == ' ':
        Encrypted_Text += ' '
    else:
        for l in range(26):
            if Initial_Text[j] == Alphabet[l]:
               Encrypted_Text += Cipher[l]

Encrypted_Text = Encrypted_Text[len(Initial_Text):]

print(f'Encrypted Text : {Encrypted_Text} ')
