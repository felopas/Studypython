numerot = int(input("Insira o número para ver a tabuada dele "))
print('a tabuada de {} é:'.format(numerot))
for n1 in range(1,11):
        resultado = numerot* n1
        print(f'{numerot} x {n1} = {resultado}')
    