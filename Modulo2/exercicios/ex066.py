'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor "999", que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

num = 0
soma = 0
contNum = 0

while True:
    num = int(input('Digite um número inteiro: '))
    if num == 999:
        break
    soma += num
    contNum += 1

print(f'A soma de {contNum} valor(es) foi {soma}!')
