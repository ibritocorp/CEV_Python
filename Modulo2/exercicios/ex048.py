'''
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''

soma = 0

for cont in range(1, 501):
    if cont % 2 != 0 and cont % 3 == 0:
        soma += cont
print(f'A soma dos números ímpares múltiplos de três é: {soma}.')
