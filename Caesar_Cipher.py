print('Caesar Cipher:')
print('(-) for left rotation')
print('key * (-1) for decryption')
print('text needs to be written in upper case letters')

Plain = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

PlainText = input('Initial Text : ')
Key = int(input('Key = '))

if Key >= 26 :
    while Key >= 26:
        Key -= 26
elif Key <= -26:
    while Key <= -26:
        Key += 26

if Key >= 0:
    Cipher = Plain[Key:] + Plain[:Key-26]
else:
    Cipher = Plain[Key+26:] + Plain[:Key]

CipherText = ''

for j in range(len(PlainText)):
    if PlainText[j] == ' ':
        CipherText += ' '
    else:
        for l in range(26):
            if PlainText[j] == Plain[l]:
               CipherText += Cipher[l]

print(f'Cipher : {Cipher}')
print(f'Cipher Text : {CipherText} ')
