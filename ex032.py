frase = str(input('Digite uma frase: ')).upper().strip()
print(f'Existem {frase.count("A") } letras A.')
print(f'A primeira letra "A" aparece na posição {frase.find("A") + 1}.')
print(f'A ultima letra "A" aparece na posição {frase.rfind("A") + 1}.')
