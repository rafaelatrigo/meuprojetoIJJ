"""Faça um for e imprima na tela todos os numeros de 1 até 1000. 
Depois, crie uma estrutura condicional para descobrir e printar apenas os números que forem par."""

"""for i in range (1,1001):
    if i % 2 == 0:
        print(i)  """


"""Crie a estrutura de uma tabuada para um valor inserido. 
O resultado deverá ser printado do valor multiplicado de 1 a 10. 

numero = int(input("Digite um valor: "))
for i in range (1,11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")"""

"""Agora crie um script para com uma lista de frutas, e outra lista com o nome alergias. 
Insira uma fruta da lista de frutas na lista de alergias. 

Depois crie um for para cada item da lista passar por uma verificação 
em uma estrutura condicional para verificar se está essa fruta está contida na lista de alergias. 
Caso a fruta esteja na lista, imprima na tela o nome dela. """

fruta = ["maçã", "banana", "laranja", "mamão"]
alergias = ["banana", "cacau", "laranja", "melancia"]

for f in fruta:
    if f in alergias:
        print(f)

