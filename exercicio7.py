#Exercicio 7
""" Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.

Calcule e mostre o total de seu salário total no referido mês, sabendo-se que são descontados 11% para o
imposto de renda, 8% para o INSS e 5% para o sindicato. Faça com que o programa que nos dê: salário
bruto, quanto pagou de INSS, quanto pagou de IR, quanto pagou de sindicato e o salário líquido, conforme
tabela abaixo:

    + Salário Bruto: R$

IR (11%): R$

INSS (8%): R$

Sindicato (5%): R$

= Salário líquido: R$ ."""

saudacao = input("Bem vindo ao programa de calculo de salario! \nDeseja entrar?(Sim ou Não)\n")
entrada = ""
if(saudacao.lower() == "sim"):
    while (entrada.lower()!= "nao"):
        valorHora = int(input("Quanto voce ganha por horas?\n"))
        horaTrab = int(input("Quantas horas trablhadas?\n"))
        salarioBruto = valorHora * horaTrab
        impRenda = salarioBruto* 11/100
        inss = salarioBruto* 8/100
        sindicato = salarioBruto* 5/100
        salarLiq = salarioBruto - impRenda - inss - sindicato
        print("Salario Bruto é: ",salarioBruto,"\n Ir = ",impRenda,"\nInss: ",inss,"\nSindicato: ",sindicato,"\nSalário Líquido: R$ ",salarLiq)

        entrada = input("Deseja continuar com novo salario? (sim ou nao)\n")
        if(entrada == "nao"):
            print('Até mais')
else:
    print("Até mais")
    exit
