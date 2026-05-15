
#* Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atíngida:
#* Média abaixo de 5.0: REPROVADO
#* Média entre 5.0 e 6.9: RECUPERAÇÃO
#* Média 7.0 ou superior: APROVADO

from statistics import mean

nota_1 = float(input('Informe a primeira nota: '))
nota_2 = float(input('Informe a segunda nota: '))
media = mean([nota_1, nota_2])


if media < 5.0:
	print(f'Sua média é {media} Você foi Reprovado.')


elif media >= 5.0 and media < 6.9:
	print(f'Sua média é {media} Você esta de Recuperação.')


else:
	print(f'Sua média é {media} Você foi Aprovado.')