"""import requests

response = requests.get('https://viacep.com.br/ws/01001000/json/')
data = response.json()

print(data['bairro'])

import pandas as pd

data = {
    'Nome': ['João','Marta', 'Ary', 'Matheus', 'Michelle'],
    'Idade': [51, 37, 23, 24, 33],
}
df = pd.DataFrame(data)
print(df[df['Idade']>30])

import pandas as pd

df = pd.read_csv("dados_ficticios.csv")
for i, linha in df.iterrows():
    print(linha['nome'], linha['renda'])"""

import pandas as pd
from faker import Faker
faker = Faker('pt-br')
data = {
    'Nome': [faker.name(), faker.name()],
    'Cidade': [faker.address(), faker.name()],
}

df = pd.DataFrame(data)
print(df)
df.to_csv("novaplaniha.csv")
