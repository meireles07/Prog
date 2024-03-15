import random

def main():
    vida_a = 100
    att_a = random.randint(10, 20) 
    deff_a =  random.randint(1, 5)

    vida_m = random.randint(60, 80)
    att_m = random.randint(20 ,30)

    print("Aventureiro: vida", vida_a, "- att", att_a, "- def", deff_a)
    print("Monstro: vida", vida_m, "- att", att_m)
    rodada = 1

    while vida_a>0 and vida_m>0 :
        print("Rodada", rodada)

        rodada += 1

        dano_a = random.randint(1, att_a)
        vida_m -= dano_a
        print("Aventureiro: vida", vida_a, "- att", att_a, "- def", deff_a)

        dano_m = random.randint(1, att_m) - deff_a
        vida_a -= dano_m
        print("Monstro: vida", vida_m, "- att", att_m)

        if vida_m <= 0:
            print("O monstro morreu!")
            break

        if vida_a <= 0:
            print("O aventureiro morreu!")
            break


main()






    



