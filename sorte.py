from random import randint
from time import sleep
print('-='*38)
print('                     Estou com sorte')
print('-='*38)
print('Olá, bem vindo ao game')
print('O premio para quem ganhar da maquina é de R$ 55.000')
jogador = int(input('Escolha um número de 0 a 9: '))#o jogador vai digitar o numero escolhido e a maquina ira armazenar na memoria
print('Agora é a minha vez...')
print('ESTOU PENSANDO EM UM NúMERO...')
sleep(2)
print('pensei!!!')
pc = randint(0, 9) # o computador vai pensar um numero
print('Resultado da Aposta...')
sleep(3)
if pc == jogador:
    print('Parabêns você ganhou o Prêmio de R$ 55.000, o número escolhido foi o: {}'.format(pc))
else:
    print('Que pena não foi desta vez,o número que pensei foi {} e não {} tente novamente'.format(pc, jogador))
print('-='*38)
