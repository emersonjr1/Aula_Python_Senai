''' João, papo de pescador, homem de bem, comprou microcomputador para controlar
o rendimento diário de seu trabalho.

Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento
de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por
quilo excedente.

João precisa que você faça um programa que leia a variável peso (peso de peixes) e
calcule o excesso.

Gravar na variável excesso a quantidade de quilos além do limite e na variável multa
o valor da multa que João deverá pagar. Imprima os dados do programa com
mensagens adequadas.'''


diario = input("Joao foi pescar hoje?\n")


if(diario.lower() == "sim"): 
    kiloPesca = int(input("Quantos quilos pegou?"))
    kiloPerm = 50
    if(kiloPesca >= 50):
        kiloResto = kiloPesca - kiloPerm 
        multa = kiloResto *4
        print(f"Voce pescou {kiloResto} Kg a mais do que o permitido. Sua multa será R$ {multa:.2f}")
    else:
        print("Pesca dentro do permitido")
else:
    print("Volte aqui quando depois da pesca")
