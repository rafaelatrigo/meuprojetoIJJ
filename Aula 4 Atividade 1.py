"""
Desafio: Fazer um programa que some 4 notas e, no final, tenha a média aritmética dessas notas.
O que seu programa deve conter:

Um input onde cada interação tenha um texto.
No final, seu programa deverá ter o output:
“Olá, Caique! Sua média é: 10 pontos”
"""

nome = input("Digite o nome da pessoa: ")

# Solicita as quatro notas da pessoa
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Calcula a média das notas
media = (nota1 + nota2 + nota3 + nota4) / 4

# Exibe o nome da pessoa e a média das notas
print(f"Olá, {nome}! Sua média é {media} pontos.")
