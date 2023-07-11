import random
from time import sleep
print('-=-'*18)
print('VOU PENSAR EM UM NÚMERO DE 0 A 10, TENTE ADIVINHAR...')
print('-=-'*18)
jogador = int(input('QUAL NÚMERO VOCÊ PENSOU??? '))
computador = random.randint(0, 10)
print('PROCESSANDO...')
sleep(2)
if computador == jogador:
    print(f'PARABÊS VOCÊ GANHOU, O NUMERO QUE ESCOLHI FOI {computador}')
else:
    print(f'EU GANHEI, O NUMERO QUE ESCOLHI FOI {computador}')
