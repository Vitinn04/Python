prod = float(input('Qual o preço do produto R$:'))
aVista = prod - (prod * 10 / 100)
parcela = prod + (prod * 8 / 100)
print(f'Se o produto for pago a vista o preço será R$:{aVista}, mas se for pago de forma parcelada o preço será R$:{parcela}')