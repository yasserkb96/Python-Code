print('Caesar Cipher:')
print('text needs to be written in upper case letters')

Plain_Text = input('Plain Text : ')
Key = int(input('Key = '))

Plain = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

Cipher_Text = ''

for j in range(len(Plain_Text)):
    if Plain_Text[j] == ' ':
          Cipher_Text += ' '
    else:
        for l in range(26):
            if Plain_Text[j] == Plain[l]:
               Cipher_Text += Plain[(l+Key) % 26]

print(f'Cipher Text : {Cipher_Text} ')
