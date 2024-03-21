"""
AC3 Victor Machado, programação estruturada
Bernardo Meireles
Triângulo , dia da semana e calculadora
"""

a = float(input("Valor do lado A:"))
b = float(input("Valor do lado B:"))
c = float(input("Valor do lado C:"))

def determina_tipo_triangulo(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
      return "Não é um Triângulo!"
    if a == b == c:
      return "Triângulo Equilátero"
    if a==b or a==c or b==c:
      return "Triângulo Isóceles"
    if a != b or a != c or b != c :
       return "Triângulo Escaleno"

print(determina_tipo_triangulo(a, b, c))

""""
EXERCÍCIO 1 ( TRIÂNGULOS )
"""

dia = float(input("Escolha um número de 1 a 7 indicando o dia da semana:"))

def dia_semana(dia):
   if dia == 1:
    return "Domingo"
   if dia == 2:
    return "Segunda-Feira"
   if dia == 3:
    return "Terça-Feira"
   if dia == 4:
    return "Quarta-Feira"
   if dia == 5:
    return "Quinta-Feira"
   if dia == 6:
    return "Sexta-Feira"
   if dia == 7:
    return "Sábado"
   else:
     return "ERROR"

print(dia_semana(dia))

""""
EXERCÍCIO 2 ( DIA DA SEMANA )
"""

num1 = float(input("Informe um número:")) 
num2 = float(input("Informe outro número:")) 
operacao_perg = (input("Informe a operação, sendo elas (soma, subtracao, multiplicacao e divisao):"))


def main(operacao_perg):
    if operacao_perg == "soma":
        return num1 + num2
    if operacao_perg == "subtracao":
        return num1 - num2
    if operacao_perg == "multiplicacao":
        return num1 * num2
    if operacao_perg == "divisao":
        return num1 / num2
    else:
        return "Operação Inválida"

print(main(operacao_perg))

""""
EXERCÍCIO 3 ( CALCULADORA SIMPLES )
"""
