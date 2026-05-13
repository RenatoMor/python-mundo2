# $ _Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
# $ • O primeiro valor é Maior
# $ • O segundo valor é Maior
# $ • Não existe valor maior, os dois são iguais

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print("O primeiro número é maior.")

elif num1 < num2:
    print("O segundo número é o maior.")

else:
    ("Não existe número maior, os dois valores são iguais.")
