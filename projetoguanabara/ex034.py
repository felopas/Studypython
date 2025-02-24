triangulo1 = float(input('digite o tamanho do lado1: '))
triangulo2 = float(input('digite o tamanho do lado2: '))
triangulo3 = float(input('digite o tamanho do lado3: '))

maiorl = max(triangulo1,triangulo2,triangulo3)
menor1,menor2 = sorted([triangulo3,triangulo1,triangulo2])[:2]
if maiorl < menor1 + menor2:
    print('da para fazer um triangulo')
else:
    print(' n é possivel fazer um triangulo')