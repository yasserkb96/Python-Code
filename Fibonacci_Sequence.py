print('Fibonacci Sequence')

N = int(input('length of the sequence = '))

Sequence = [0,1]

for k in range(2,N):
    Sequence.append(int(Sequence[k-1]) + int(Sequence[k-2]))

print(f'Sequence = {Sequence}')
