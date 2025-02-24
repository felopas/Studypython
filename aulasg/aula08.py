import os 
os.system('cls' if os.name == 'nt' else 'clear')

import math
num = int(input('digite um numero: '))
raiz = math.sqrt(num)
print(f'a raiz do numero {num} é {math.floor(raiz)}')
print(f'a raiz do numero {num} é {math.ceil(raiz)}')
print(f'a raiz do numero {num} é {raiz}')
print(f'a raiz do numero {num} é {raiz:.2f}')