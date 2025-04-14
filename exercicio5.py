saudacao = input("Bem vindo ao programa de conversão de temperatura(ºC para ºF)\nDeseja entrar?\n")
entrada = ""
if(saudacao.lower() == "sim"):
    while (entrada.lower()!= "nao" ):
            grauC = int(input("Quantos graus? \n Digite:  "))
            grauF = 9/5 * grauC +32
            print("Valor em Fº é  ",grauF," Fº")

            entrada = input('Deseja Continuar? \n Digite "nao" para para sair.')
    print("Até mais")

else:
    print("Até mais")
    exit
