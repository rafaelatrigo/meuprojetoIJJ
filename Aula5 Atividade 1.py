"""
USANDO IF: Construa um script para verificar se o usuário tem uma idade maior que 18 anos, se tiver, 
imprima na tela "Indivíduo possui idade mínima para dirigir"
"""

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Indivíduo possui idade mínima para dirigir")
else:
    print("Indivíduo não possui idade mínima para dirigir")
    