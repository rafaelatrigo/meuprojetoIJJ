"""
USANDO IF: Construa um script para verificar se o usuário tem uma idade maior que 18 anos, se tiver, 
imprima na tela "Indivíduo possui idade mínima para dirigir"
"""

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Indivíduo possui idade mínima para dirigir")
elif idade >= 16 and idade <= 17: 
    print("Indivíduo tem entre 16 e 17 anos e ainda NÃO está apto para dirigir")    
else:
    print("Indivíduo NÃO  possui idade mínima para dirigir")

    