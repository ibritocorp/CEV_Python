"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Exp.:
Digite um número: 1834

unidade: 4
dezena: 3
centena: 8
milhar: 1
"""

n = str(input('Digite um número: '))
qtdcaractere = len(n)
print(f'Unidade: {n[qtdcaractere]}\nDezena: {n[qtdcaractere - 1]}\nCentena: {n[qtdcaractere - 2]}\nMilhar: {n[qtdcaractere - 3]}')