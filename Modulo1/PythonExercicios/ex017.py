# Leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

from math import pow, sqrt

catOposto = float(input('Digite o comprimento do Cateto Oposto: '))
catAdjacente = float(input('Digite o comprimento do Cateto Adjacente: '))
hipotenusa = sqrt(pow(catOposto, 2) + pow(catAdjacente, 2))
print(f'A hipotenusa é {hipotenusa}')