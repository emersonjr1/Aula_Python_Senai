saudacao = input("Bem vindo ao programa \n Deseja entrar?\n")
entrada = ""
if(saudacao.lower() == "sim"):
    while (entrada.lower()!= "nao" ):
            preco = int(input("Qual o preço da mercadoria? \n Digite um numero\n"))
            desconto = int(input("Digite o valor do desconto para pagamentos a vista.\n"))
            valor_total = preco - (preco* (desconto / 100))
            print("Valor total: R$ ", valor_total)

            entrada = input('Deseja Continuar? \n Digite "nao" para para sair.')
    print("Até mais")

else:
    print("Até mais")
    exit
