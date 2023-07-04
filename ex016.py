prod = float(input('Digite o preço do produto R$: '))
desconto = prod * 5 / 100
precoFinal = prod - desconto
print(f'O prduto que antes valia R$:{prod :.2f} agora vale R$:{precoFinal :.2f}, o desconto foi de R$:{desconto :.2f}')