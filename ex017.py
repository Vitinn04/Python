salario = float(input('Digite o valor do salário do seu funcionário R$: '))
aumento = salario * 15 / 100
salarioFinal = salario + aumento
print(f'O salário saiu de R$:{salario :.2f} para R$:{salarioFinal :.2f}, o aumento foi de R$:{aumento :.2f}')