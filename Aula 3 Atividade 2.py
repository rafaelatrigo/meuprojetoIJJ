"""
A loja "ROUPAS SA" tem 2000 clientes e quer enviar mensagens nominais a cada um. 
A mensagem seria a seguinte:

Olá, PAULA MARTINS. Em JANEIRO você realizou uma compra no valor de R$500,00 e ganhou um desconto 
de 10% em sua próxima compra. Use o cupom PAULAÉ10.
"""

nome = "Paula"
mes = "Janeiro"
compra ="500,00"
desconto = "10"
cupom = "PAULA10"

print ("Olá, " +nome+ ". Em " +mes+ " você realizou uma compra no valor de R$"+compra+ " e ganhou um desconto de " +desconto+ "em sua próxima compra. Use o cupom " +cupom)

#print(type(cupom)) # retorna o tipo da variavel
# exemplo de "format" nome e sobrenome seriam variaveis. print ('meu nome é ' {a}, meu sobrenome é {b}, format(a=nome, b=sobrenome))

"""
pra mudar o tipo da variável usamos
int
float
str 

exemplo: 
cupom = int ("PAULA10")
"""

