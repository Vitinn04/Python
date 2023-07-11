km = float(input('Qual foi a quantidade de kilometros rodados na viagem? '))
if km <= 200:
    print(f'O preço da viagem é R${km*0.50:.2f}')
elif km > 200:
    print(f'O preço da viagem é R${km*0.45:.2f}')
