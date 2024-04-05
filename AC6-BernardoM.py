"""
AC6 Victor Machado, programação estruturada
Bernardo Meireles
"""

"""
1 - HELLO WORLD!
"""

print("Hello World!")

"""
2 - EXTREMAMENTE BASICO
"""
print("-" * 40)

a = int(input("A:"))
b = int(input("B:"))

print("X =", a+b)

"""
3 - CALCULO SIMPLES
"""
print("-" * 40)

a1 = int(input("Código da Peça 1:"))
a2 = int(input("Números de Peças 1:"))
a3 = float(input("Valor Unitário de Cada Peça 1:"))

b1 = int(input("Código da Peça 2:"))
b2 = int(input("Números de Peças 2:"))
b3 = float(input("Valor Unitário de Cada Peça 2:"))


a = a2 * a3
b = b2 * b3

print("VALOR A PAGAR: R$", a+b)

"""
4 - O MAIOR
"""
print("-" * 40)

a = int(input("Numero:"))
b = int(input("Numero:"))
c = int(input("Numero:"))

maiorab = ( a + b + abs(a-b)) / 2

maior_final = ( maiorab + c + abs(maiorab-c)) / 2

print(maior_final, "eh o maior")

"""
5 - DISTANCIA ENTRE DOIS PONTOS
"""
print("-" * 40)

import math

x1 = float(input("X1:"))
y1 = float(input("Y1:"))
x2 = float(input("X2:"))
y2 = float(input("Y2:"))

distancia = (x2-x1)**2+(y2-y1)**2
final = math.sqrt(distancia)

print(round(final,4))