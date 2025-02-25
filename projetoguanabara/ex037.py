import os

os.system('cls' if os.name == 'nt' else 'clear')

print("Terminal limpo! Iniciando o teste...")


num = int(input('escolha um numero:'))
tipo = int(input('escolha qual sera baseado a conversão \n 1. binário \n 2. octal \n 3. hexadecimal\n :'))

bi = bin(num)
oct = oct(num)
hex = hex(num)

if tipo == 1:
    print(f'\n o conversão em bináro é: {bi}\n')
elif tipo == 2:
    print(f'\n a conversão em octal é: {oct}\n')
else:
    print(f'\n a conversão em hexadecimal é: {hex}\n')