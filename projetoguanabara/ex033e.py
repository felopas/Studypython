a = int(input('primeiro valor:'))
b = int(input('segundo :'))
c = int(input('terceiro valor:'))
menor = a 
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

maior = a 
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print(f'o maior valor foi:{maior}')
print(f'o menor valor foi:{menor}')