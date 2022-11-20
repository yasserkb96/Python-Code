print('Caesar Cipher Brute Force Attack:')

def Caesar_Cipher(Encrypted_Text,Key):

    Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    Cipher = Alphabet[Key:]+Alphabet[:Key-26]

    Text = Encrypted_Text

    for j in range(len(Encrypted_Text)):
        if Encrypted_Text[j] == ' ':
            Text += ' '
        else:
            for l in range(26):
                if Encrypted_Text[j] == Alphabet[l]:
                   Text += Cipher[l]

    Text = Text[len(Encrypted_Text):]

    return Text

Encrypted_Text = input('Encrypted Text :')

for N in range(1,26):
    print(f'Possible_Text({N}) : {Caesar_Cipher(Encrypted_Text,N)}')
