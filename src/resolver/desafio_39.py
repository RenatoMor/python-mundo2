"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se a hora de se alistar ou seja, passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

ano_nascimento = int(input("Ínforme o seu ano de nascimento: "))

ano_atual = 2026
idade_alistamento = 18
idade = ano_atual - ano_nascimento
periodo = idade - idade_alistamento

print(f"Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}")
print(f"Seu alistamento será em {idade}")


if periodo < 0:
    print(f"Ainda faltam {periodo} anos para oalistamento")

elif periodo > 0:
    print(f"O periodo do seu alistamento esta atrasado em {periodo} anos.")

else:
    print("Você já pode se alistar.")
