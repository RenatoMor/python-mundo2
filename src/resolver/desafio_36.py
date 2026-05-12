# * Escreva um program para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

# $ Calcule o valor da prestação mensal, sabendo que pode exceder 30% do salário ou então o empréstimo será negado.

# Valor do empréstimo
# Valor da casa
# Salario do comprador

# Quantidade de anos para pagar (meses)


valor_da_casa = 0
valor_do_emprestimo = 0
salario_do_comprador = 0

valor_da_casa = float(input("Informe o valor da casa: R$ "))
salario_do_comprador = float(input("Informe o seu salário: R$ "))
quantidade_de_anos_para_pagar = int(input("Em quantos anos quer pagar o imóvel: "))

percentual_do_salario = salario_do_comprador * 0.3
print(f"30% do seu salário é R$ {percentual_do_salario:.2f}")
valor_prestacao_mensal = valor_da_casa / (quantidade_de_anos_para_pagar * 12)
print(f"O valor da prestação mensal é de R$ {valor_prestacao_mensal:.2f}")


if valor_prestacao_mensal <= percentual_do_salario:
    print("Empréstimo aprovado!")

elif valor_prestacao_mensal > percentual_do_salario:
    print("Empréstimo negado!")
