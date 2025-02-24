frase = input('escreva uma frase: ')
frasef = frase.lower().strip()

f = frase.lower().count('a')
print(f'A sua frase contem {f} a')
frase2 = frase.find('a')
print(f'o primeiro a é na posição: {frase2 + 1} ')
frase3 = frase.rfind('a')
print(f'o primeiro a é na posição: {frase3 + 1} ')