"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se a hora de se alistar ou seja, passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date

nasc = int(input("Informe o ano de nascimento: "))


atual = date.today().year
idade = atual - nasc
alistamento = nasc + 18

print(f"Quem nasceu em {nasc} tem {idade} anos em {atual}.")

if alistamento > atual:
    print(f"Ainda faltam {alistamento - atual} anos para o seu alistamento.")
    print(f'Seu alistamento será em {alistamento}.')

elif alistamento < atual:
    print(f"Você já deveria ter se alistado há {atual - alistamento} anos.")
    print(f'Seu alistamento foi em {alistamento}.')

elif alistamento == atual:
    print("Você já pode se alistar.")

else:
    print("Data inválida.")

          

