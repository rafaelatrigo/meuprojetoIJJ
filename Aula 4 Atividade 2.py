"""
Desafio: Faça um código que permita, ao inserir um valor, o retorno de 5 outputs, sendo eles:

primeiro output: deve apresentar como resultado o dobro do valor inserido;
segundo output: deve apresentar como resultado o triplo do valor inserido;
terceiro output: deve apresentar como resultado o valor inserido ao quadrado;
quarto output: deve apresentar como resultado a raiz quadrada do valor inserido;
quinto output: deve apresentar como resultado a raíz cúbica do valor inserido.

"""
valor = float(input("Digite um valor: "))

# Calcula os resultados
dobro = valor * 2
triplo = valor * 3
quadrado = valor ** 2
raiz_quadrada = valor**(1/2)
raiz_cubica = valor**(1/3)

# Exibe os cinco resultados
print(f"1º Output (dobro do valor): {dobro}")
print(f"2º Output (triplo do valor): {triplo}")
print(f"3º Output (valor ao quadrado): {quadrado}")
print(f"4º Output (raiz quadrada do valor): {raiz_quadrada}")
print(f"5º Output (raiz cúbica do valor): {raiz_cubica}")
