dia = int(input('Digite o numero de dias pelos quais o carro foi alugado: '))
km = float(input('Digite o numero de KMs rodados: '))

dias = dia * 60.0
KMs = km * 0.15
preço = dias + KMs
print(f'O preço a ser pago é R$:{preço :.2f}')