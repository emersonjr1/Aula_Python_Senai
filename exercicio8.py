#Exercicio
"""Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro
desta área para o usuário."""

saudacao = input("Bem vindo ao programa de calculo da área de um quadrado.\nDeseja entrar?(sim ou nao)\n")

if(saudacao == "sim"):

    while(saudacao != "nao"):
        lado1 = int(input("Digite o tamanho do primeiro lado do quadrado\n"))
        lado2 = int(input("Digte o tamanho do segundo lado do quadrado\n"))

        area = lado1 * lado2

        dobro = area * 2

        print("A area do quadrado é ",area,"e o dobro é ",dobro,".")

        saudacao = input("Deseja verificar um novo quadrado? (sim ou não) \n")
        if(saudacao != "sim"):
            print("Até mais!")
else:
    print("Até mais!")
