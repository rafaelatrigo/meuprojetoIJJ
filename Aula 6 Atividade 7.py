"""O instituto Joga Junto vai checar todos os emails existentes utilizados pelos usuários. 
Para isso sua equipe precisará criar  um código para verificar se o email inserido pelo usuário 
tem o @jogajuntoinstituto.org no texto. 

Crie um input para verificar esse texto."""

verifica = False
teste = "@jogajuntoinstituto.org"

while True:
    email = input('Digite seu e-mail: ')
    if teste in email:
        verifica = True
        print("E-mail válido")
        break  
    else:
        print("Email inválido")
