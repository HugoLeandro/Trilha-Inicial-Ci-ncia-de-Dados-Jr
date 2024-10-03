import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%matplotlib inline

# 1. Criação do DataFrame
from io import StringIO

dados = """ID,Nome do Curso,Quantidade de Vendas,Preço Unitário,Data
1,Introdução à Programação em Python,50,39.90,2023-01-01
2,Desenvolvimento Web com HTML e CSS,30,59.90,2023-01-02
3,JavaScript Avançado: Frameworks e Bibliotecas,20,79.90,2023-01-03
4,Introdução ao Machine Learning,15,99.90,2023-01-04
5,Desenvolvimento Mobile com React Native,25,69.90,2023-01-05
6,Arquitetura de Microserviços,12,89.90,2023-01-06
7,Banco de Dados SQL e NoSQL,18,79.90,2023-01-07
8,Segurança da Informação: Fundamentos,10,109.90,2023-01-08
9,Cloud Computing com AWS,22,99.90,2023-01-09
10,DevOps: Integração e Entrega Contínua,8,119.90,2023-01-10
11,Desenvolvimento Web com HTML e CSS,20,59.90,2023-01-11
12,JavaScript Avançado: Frameworks e Bibliotecas,15,79.90,2023-01-12
13,Introdução ao Machine Learning,10,99.90,2023-01-13
14,Desenvolvimento Mobile com React Native,18,69.90,2023-01-14
15,Arquitetura de Microserviços,8,89.90,2023-01-15
16,Banco de Dados SQL e NoSQL,12,79.90,2023-01-16
17,Segurança da Informação: Fundamentos,5,109.90,2023-01-17
18,Cloud Computing com AWS,15,99.90,2023-01-18
19,DevOps: Integração e Entrega Contínua,6,119.90,2023-01-19
20,Introdução à Programação em Python,45,39.90,2023-01-20
21,Desenvolvimento Web com HTML e CSS,25,59.90,2023-01-21
22,JavaScript Avançado: Frameworks e Bibliotecas,18,79.90,2023-01-22
23,Introdução ao Machine Learning,12,99.90,2023-01-23
24,Desenvolvimento Mobile com React Native,20,69.90,2023-01-24
25,Arquitetura de Microserviços,10,89.90,2023-01-25"""

df = pd.read_csv(StringIO(dados))

# 2. Exploração de Dados
df['Data'] = pd.to_datetime(df['Data'])

# Exibir as primeiras linhas e informações básicas
print(df.head())
print("\nNúmero de linhas e colunas:", df.shape)
print("\nTipos de dados:\n", df.dtypes)

# 3. Estatísticas Descritivas
print("\nEstatísticas Descritivas:")
print(df.describe())

# 4. Visualização de Dados
sns.set(style="whitegrid")

# 4.1 Gráfico de Barras
vendas_por_curso = df.groupby('Nome do Curso')['Quantidade de Vendas'].sum().reset_index()

plt.figure(figsize=(12,6))
sns.barplot(x='Quantidade de Vendas', y='Nome do Curso', data=vendas_por_curso, orient='h')
plt.title('Quantidade Total de Vendas por Curso')
plt.xlabel('Quantidade de Vendas')
plt.ylabel('Nome do Curso')
plt.show()

# 4.2 Gráfico de Dispersão
plt.figure(figsize=(8,6))
sns.scatterplot(x='Preço Unitário', y='Quantidade de Vendas', data=df)
plt.title('Preço Unitário vs Quantidade de Vendas')
plt.xlabel('Preço Unitário (R$)')
plt.ylabel('Quantidade de Vendas')
plt.show()

# 5. Desafios Propostos
# 5.1 Receita Total
df['Receita'] = df['Quantidade de Vendas'] * df['Preço Unitário']
receita_total = df['Receita'].sum()
print("\nReceita Total Gerada: R$ {:.2f}".format(receita_total))

# 5.2 Curso Mais Vendido
vendas_totais = df.groupby('Nome do Curso')['Quantidade de Vendas'].sum()
curso_mais_vendido = vendas_totais.idxmax()
quantidade_mais_vendido = vendas_totais.max()
print("\nCurso com Maior Número de Vendas:")
print("Nome do Curso:", curso_mais_vendido)
print("Quantidade de Vendas:", quantidade_mais_vendido)

# 5.3 Distribuição das Vendas ao Longo do Tempo
vendas_por_data = df.groupby('Data')['Quantidade de Vendas'].sum().reset_index()

plt.figure(figsize=(12,6))
sns.lineplot(x='Data', y='Quantidade de Vendas', data=vendas_por_data, marker='o')
plt.title('Distribuição das Vendas ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Quantidade de Vendas')
plt.xticks(rotation=45)
plt.show()
