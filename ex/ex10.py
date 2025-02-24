horaganha = int(input('coloque o total que vc ganha por hora:'))
horastrabalhada = int(input('coloque que vc trabalhou:'))
resultado = horaganha * horastrabalhada
IR = 11%resultado
Inss = 8% resultado
final= (resultado - (Inss + IR))

print(('Salário por hora: ') , horaganha)
print(('Total de horas trabalhadas: ') , horastrabalhada)
print(('Salário Bruto: ') , resultado)
print(('IR: ') , IR)
print(('Inss ') ,Inss)
print(('Salário líquido: ') ,final)