n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))
m = (n1 + n2)/2
print(f'A SUA MÉDIA FOI {m:.1F}')
if m >= 6.0:
    print('VOCÊ FOI APROVADO!')
else:
    print('VOCÊ FOI REPROVADO!')
