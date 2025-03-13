"""Variaveis"""

# variaveis são containers para armazenar valores de dados

"""Criando Variaveis"""

# Ao contrario de outras linguagens em python Variáveis ​​não 
# precisam ser declaradas com nenhum tipo específico e podem 
# até mesmo mudar de tipo depois de serem definidas.

# exemplo
x = 4 # x foi atribuido como um inteiro
print(type(x)) # <class 'int'>

x = 'meuNome' # x passa a ser uma string
print(type(x)) # <class 'str'>

"""Fundição / conversão"""

# podemos especificar um tipo de dados armazenado em uma 
# variavel usando conversão
x = str(3)
print(type(x)) # <class 'str'>

y = int(3)
print(type(y)) # <class 'int'>

z = float(3)
print(type(z)) # <class 'float'>

"""Obtenha o tipo de dado"""

# Você pode obter o tipo de dados de uma variável com a type()
# função, como nos exemplos acima 

""" Aspas simples ou duplas? """

# Variáveis ​​de string podem ser declaradas usando aspas 
# simples ou duplas

# exemplo
a = 'texto'
a = "texto"

"""Maiúsculas e minúsculas"""

# python é sensitivecase e difere maiúsculas de minúsculas

# exemplo
a = 123 # isso é uma variavel
A = 65.96 # isso é outra variavel
