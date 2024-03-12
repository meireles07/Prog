def eq_seg_grau(a, b, c):
    Delta = (b**2 - 4*a*c)
    Primeira = (-b + Delta**(1/2)) / (2*a)
    Segunda = (-b - Delta**(1/2)) / (2*a)
    
    print("Valor de X1:", Primeira)
    print("Valor de X2:", Segunda)


print("Equação segundo grau:")
a = float(input("Informe o valor de A :"))
b = float(input("Informe o valor de B :"))
c = float(input("Informe o valor de C :"))
eq_seg_grau(a, b, c)

"""
Ex 1 Acima ( def, eq_seg_grau: )
"""

def bissexto():
    ano = int(input("Qual o Ano:"))
    if (ano%4==0 and ano%100!=0) or (ano%400==0):
        print(True)
    else:
        print(False)

bissexto()

"""
Ex 2 Acima ( bissexto(ano) ) 
Victor - O "bissexto("ANO") com o 'ano', dentro do parenteses nao tava funcionando, então deixei so bissexto()
e não tinha certeza se podia ou não, usar print, mas não tava conseguindo nao usar o print para true e false
"""

def calcula_salario():
    valor_hora = int(input("Qual o valor por hora?: "))
    num_hora = int(input("Quantas horas trabalhou no mês?: "))
    irpf = 0.725

    print((valor_hora*num_hora) * irpf )

calcula_salario()

"""
Ex 3 Acima ( calcula_salario )
Victor - eu fiz um método de fazer * o valor de 1 - 0,275 que chegava a soma final do salário líquído mais rápido
usando entao o valor da hora * o numero de horas - o imposto de renda (*)
"""

