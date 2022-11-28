print('Caesar Cipher Brute Force Attack:')

def Caesar_Cipher(Cipher_Text,Key):

    Plain = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    Cipher = Plain[Key:] + Plain[:Key-26]

    Plain_Text = ''

    for j in range(len(Cipher_Text)):
        if Cipher_Text[j] == ' ':
            Plain_Text += ' '
        else:
            for l in range(26):
                if Cipher_Text[j] == Plain[l]:
                   Plain_Text += Cipher[l]

    return Plain_Text

Cipher_Text = input('Cipher Text :')

for N in range(1,26):
    print(f'Possible Plain Text({N}) : {Caesar_Cipher(Cipher_Text,N)}')
