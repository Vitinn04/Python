print('-=-'*9)
print('Analisador de triangulos')
print('-=-'*9)
l1 = float(input('Digite o 1° lado do triângulo: '))
l2 = float(input('Digite o 2° lado do triângulo: '))
l3 = float(input('Digite o 3° lado do triângulo: '))
if l1+l2 < l3 or l2+l3 < l1 or l1+l3 < l2:
    print(f'É possivel formar um triângulo')
else:
    print(f'Não é possivel formar um triângulo')
