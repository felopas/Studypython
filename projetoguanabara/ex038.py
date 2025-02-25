num1 = int(input('escreva um numero: '))
num2 = int(input('escreva outro numero: '))

if num1 < num2:
    print(f'o numero {num2} é maior que {num1}')
elif num2 < num1:
    print(f'o numero {num2} é menor que {num1}')
else:
    print('os dois numeros são iguais')