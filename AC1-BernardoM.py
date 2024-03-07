"""
AC1 Victor Machado, programação estruturada
Bernardo Meireles 
Ano Bissexto
"""
def eq(a, b, c):
    Delta = (b**2 - 4*a*c)
    Primeira = (-b + Delta**(1/2)) / (2*a)
    Segunda = (-b - Delta**(1/2)) / (2*a)

    print("Valor da primeira raiz:")
    print(Primeira)
    print("Valor da segunda raiz:")
    print(Segunda)

a = float(input("Informe o valor de A :"))
b = float(input("Informe o valor de B :"))
c = float(input("Informe o valor de C :"))


print(eq(a, b, c))


"""
-------------------------------------------------------
Código acima AC1 exercício 1, raizes de segundo grau
Código abaixo AC2 exercício 2, ano bissexto
-------------------------------------------------------
"""

Ano = int(input("Qual o Ano? : "))
B = (Ano%4==0) and (Ano%100!=0) or (Ano%400==0)

print(B)