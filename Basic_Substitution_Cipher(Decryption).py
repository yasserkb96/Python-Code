print('Basic Substitution Cipher Decryption:')
print('text needs to be written in upper case letters')

CipherText = input('Text : ')
Cipher = input('Cipher : ')

Plain = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

PlainText = ''

for j in range(len(CipherText)):
    if CipherText[j] == ' ':
        PlainText += ' '
    else:
        for l in range(26):
            if CipherText[j] == Cipher[l]:
               PlainText += Plain[l]

print(f'Plain Text : {PlainText} ')
