import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(co,ca)
print(f'O valor da hipotenusa é +- {hipotenusa:.2f}')
