a = input('Digite algo: ')
print(f'O tipo primitivo dessa variavel é {type(a)}')
print(f'Está em maiusculo? {a.isupper()}')  # Maiusculo
print(f'Está em minusculo? {a.islower()}')
print(f'É alfabético? {a.isalpha()}')  # Alfabético
print(f'É um numero? {a.isnumeric()}')  # Numérico
print(f'É alfanumérico? {a.isalnum()}')  # Alfanumérico
print(f'Só tem espaço? {a.isspace()}')  # Espaço
print(f'Está capitalizada? {a.istitle()}')