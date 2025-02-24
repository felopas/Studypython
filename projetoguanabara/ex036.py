vcasa = float(input('qual o valor da casa? '))
vsalario = float(input('quanto vc ganha? '))
prestano = int(input('quantos anos vc quer pagar? '))
#o valor da parcela não pode exceder 30% do salario
prestmensal = prestano * 12
casames = vcasa / prestmensal
if casames <= (vsalario  * 0.3) :
    print('vc pode fazer emprestimo')
else:
    print('vc n pode fazer emprestimo')
    print(f'o custo mensal de R${casames:2f} ficaria a cima de 30% do seu salario que é {vsalario * 0.3} ')
