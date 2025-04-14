'''
9 -  Faça um Programa que calcule o peso ideal de uma pessoa. Para isso, solicite a
altura da pessoa, o nome da pessoa. Utilize as seguintes fórmulas:

Homens – (72.7 * altura) – 58

Mulheres – (62.1 * altura) – 44.7 
'''


#exercicio 9
saudacao = input("Bem vindo ao programa de calculo de peso ideal.\n Vamos calcular seu peso ideal? (sim ou nao)\n")

pesoIdeal = ""
if(saudacao.lower() == "sim"):
    nome = input("Qual seu nome?\n")
    print("Olá, ",nome)
    sexo = input("Qual seu sexo? (Masculino ou Feminino)\n")
    altura = float(input("Digite sua altura em Metros.\n"))


    if(sexo.lower() == "masculino"):
        pesoideal = (72.7 * altura) - 58

        
    elif(sexo == "feminino"):
        pesoideal = (62.1 * altura) - 44.7

    print(f"Seu peso ideal é: ",pesoideal)
else:
    print("Até mais")
