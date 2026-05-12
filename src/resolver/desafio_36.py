# $  Escreva um program para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

# $  $ Calcule o valor da prestação mensal, sabendo que pode exceder 30% do salário ou então o empréstimo será negado.

# $ Valor do empréstimo
# $ Valor da casa
# $ Salario do comprador

# $ Quantidade de anos para pagar (meses)

casa = float(input("Informe o valor da casa: R$ "))
salario = float(input("Informe o seu salário: R$ "))
anos = int(input("Em quantos anos quer pagar o imóvel: "))
minimo = salario * 30 / 100
prestacao = casa / (anos * 12)

print(f"Limite: 30% do seu salário é R$ {minimo:.2f}")
print(f"O valor da prestação mensal é de R$ {prestacao:.2f}")


if prestacao <= minimo:
    print("Empréstimo aprovado!")

else:
    print("Empréstimo negado!")
