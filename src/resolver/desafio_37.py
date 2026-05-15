# $ Escreva um programa que leia um número interio qualquer e peça para o úsuario escolher qual será a base de conversão:

# $ 1 para binário
# $ 2 para octal
# $ 3 para hexadecimal


conversao = int(input("Informe um número inteiro: "))
print("""Escolha a base de conversão:
[1] Binário
[2] Octal
[3] Hexadecimal""")

opcao = int(input("Sua opção: "))

if opcao == 1:
    print(f"{conversao} convertido para binário é igual a {bin(conversao)[2:]}")
elif opcao == 2:
    print(f"{conversao} convertido para octal é igual a {oct(conversao)[2:]}")
elif opcao == 3:
    print(f"{conversao} convertido para hexadecimal é igual a {hex(conversao)[2:]}")
else:
    print("Opção inválida!")
