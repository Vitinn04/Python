vel = float(input('QUAL A VELOCIDADE DO CARRO? '))
if vel > 80:
    multa = (vel-80) * 7
    print(f'VELOCIDADE NÂO PERMITIDA, VOCÊ FOI MULTADO EM R${multa}!')
else:
    print(f'VELOCIDADE PERMITIDA!')
