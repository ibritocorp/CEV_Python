'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

num = 0
cont = -1
soma = 0

while num != 999:
    soma += num
    num = int(input('Digite um número inteiro: '))
    cont += 1

print(f'Você digitou {cont} número(s) e a soma dele(s) foi {soma}.')
