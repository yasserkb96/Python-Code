import random

print('Basic Substitution Cipher Encryption:')
print('text needs to be written in upper case letters')

Plain_Text = input('Plain Text : ')
Plain = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

Plain_List = list(Plain)
Plain_List_Tool = list(Plain)

Cipher_List = []

for k in range(26):
    Cipher_List.append(random.choice(Plain_List_Tool))
    Plain_List_Tool.remove(Cipher_List[k])

Cipher = ''.join(Cipher_List)

Cipher_Text = ''

for j in range(len(Plain_Text)):
    if Plain_Text[j] == ' ':
        Cipher_Text += ' '
    else:
        for l in range(26):
            if Plain_Text[j] == Plain[l]:
               Cipher_Text += Cipher[l]

print(f'Cipher : {Cipher}')
print(f'Cipher Text : {Cipher_Text} ')
