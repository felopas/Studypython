import random
print('o computador pensou em um numero de 1 a 5')
numberplayer = int(input('qual é o numero? '))
numberbot = random.randint(1, 5)
if numberbot == numberplayer:
    print('Parabéns, vc acertou')
else:
    print('infelizmente vc errou, quer tentar dnv?')