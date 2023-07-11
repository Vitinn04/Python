sal = float(input('Digite o sálario: '))
aumento10 = (sal*10)/100
aumento15 = (sal*15)/100
if sal > 1250:
    print(f'O aumento será de {aumento10}, o novo sálario será de {sal + aumento10}')
else:
    print(f'O aumento será de {aumento15}, o novo sálario será de {sal + aumento15}')
