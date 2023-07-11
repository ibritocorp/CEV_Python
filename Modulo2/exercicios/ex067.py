'''
Faça um programa que mostre a tabuada de vários números, um de cada vez para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''

num = 0

while True:
    num = int(input('Quer ver a tabuada de qual número? '))

    print('-' * 30)

    if num < 0:
        break

    for cont in range(1, 11):
        print(f'{num} x {cont} = {num * cont}')
    
    print('-' * 30)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
