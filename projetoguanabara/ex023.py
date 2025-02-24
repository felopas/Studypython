num = int(input('escreva um numero: '))
u = num //1%10
u1 = num //10%10
u2 = num //100%10
u3 = num //1000%10
print(f'Analisando o numero{num}')
print(f'unidade: {u}')
print(f'Dezena: {u1}')
print(f'Centena: {u2}')
print(f'Milhar: {u3}')
