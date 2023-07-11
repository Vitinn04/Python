import math
angulo = float(input('Digite o angulo: '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O seno desse ângulo é {seno:.2f}')
print(f'O coseno desse ângulo é {coseno:.2f}')
print(f'A tangente desse ângulo é {tangente:.2f}')