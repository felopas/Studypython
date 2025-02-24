import math
oposto = int(input('coloque o cateto oposto: '))
adjacente = int(input('coloque o cateto adjacente: '))
hipotenusa = math.sqrt((pow(oposto,2)+pow(adjacente,2)))
print(f'a hipotenusa é {hipotenusa:.2f}')