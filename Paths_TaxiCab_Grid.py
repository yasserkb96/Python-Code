def factorial(N):
    b = 1
    for k in range(1,N+1):
        b = b * k
    return b

def Sum_of_abs_values(L):
    s = 0
    for k in range(len(L)):
        s = s + abs(int(L[k]))
    return s

def Product_of_list_values(L):
    p = 1
    for k in range(len(L)):
        p = p * int(L[k])
    return p

print('Number of shortest possible paths between two nodes in an N dimensional TaxiCab grid:')
print('The values to fill the list of coordinates are how far away is a node from the other nodes in terms of grid lines')
N = int(input('Grid\'s number of dimensions = '))

Coordinates = []
Factorials_of_abs_values = []

for k in range(N):
    Coordinates.append('')
    Factorials_of_abs_values.append('')
    Coordinates[k] = input(f'X{k+1} = ')
    Factorials_of_abs_values[k] = factorial(abs(int(Coordinates[k])))

print(f'Number of shortest possible paths = {factorial(Sum_of_abs_values(Coordinates))//Product_of_list_values(Factorials_of_abs_values)}')
