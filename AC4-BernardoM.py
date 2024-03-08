
def ler_nome():
    return input("Seu nome:")

def ler_notas():
    ap1 = float(input("Informe o valor da Ap1:"))
    ap2 = float(input("Informe o valor da Ap2:"))
    asub = float(input("Informe o valor da Asub:"))
    ac = float(input("Informe o valor da Ac:"))
    return ap1,ap2,asub,ac

def analisar_subst(ap1, ap2, asub):
    if asub > ap1:
        return asub, ap2
    if asub > ap2:
        return asub, ap1
    return ap1, ap2

def calcular_media(ap1, ap2, asub, ac):
    prova1, prova2 = analisar_subst(ap1, ap2, asub)
    return (prova1 + prova2) * 0.4 + ac * 0.2

def aluno_foi_aprovado(media):
    return media >= 7

def notas_sao_validas(ap1, ap2, asub, ac):
    if 0 <= ap1 <= 10:
        return True
    if 0 <= ap2 <= 10:
        return True
    if 0 <= asub <= 10:
        return True
    if 0 <= ac <= 10:
        return True

def main():
    nome = ler_nome()
    if nome:
        ap1 , ap2 , asub, ac = ler_notas()
        if notas_sao_validas(ap1, ap2, asub, ac):
            media = calcular_media(ap1, ap2, asub, ac)
            print("Média Final:", media)
            if aluno_foi_aprovado(media):
                print("Aluno foi aprovado.")
            else:
                print("Aluno foi reprovado.")

main()