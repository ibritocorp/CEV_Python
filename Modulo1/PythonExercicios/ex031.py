"""
Desenvolva um programa que pergunte a distância de uma viagem em km, calcule o preço da passagem cobrando R$0.50 por km para viagens de até 200km e R$0.45 para viagens mais longas.
"""

distancia = float(input('Digite a distância da viagem em km: ').strip())
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print(f'O preço da passagem é R${preco:.2f}')