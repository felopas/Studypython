largura = int(input('largura'))
altura = int(input('altura'))

metro = largura * altura
# 1 litro para 2m²
tinta = metro / 2
print(f'vai precisar de {tinta} litro para pintar a parede')