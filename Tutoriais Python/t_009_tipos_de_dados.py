"""Tipo de dados"""
# Variáveis ​​podem armazenar dados de diferentes tipos, e 
# diferentes tipos podem fazer coisas diferentes.

# O Python tem os seguintes tipos de dados incorporados por 
# padrão, nestas categorias:

# textos : str
# Numericos : int, float, complex
# Sequenciais: list, tuple, range
# Mapeamento: dict
# Conjuntos: set, frozenset
# Booleanos: bool
# Binários: bytes, bytearray, memoryview
# Nenhum Tipo: None

"""Obtendo tipo de dados"""

# Para indentificar o tipo de dado de qualquer objetos se usa 
# a função 'type()'
x = 5
obter_tipo_de_dado = type(x)
print(obter_tipo_de_dado) # Saida: <class 'int'>

"""Definindo o tipo de dado"""

# O tipo de dado é definido automaticamente quando atribuimos 
# um valor a variavel, ou seja não precisamos declarar o tipo

texto = "Um texto - str"
inteiro = 10
real = 12.4
numeros_complexos = 1j
lista = ["maçã", "banana", "morango"]
tupla = ("uva", "jabuticaba", "manga")
sequencia_numerica = range(10)
dicionario = {"chave1":"valor1", "chave2": "valor2"}
conjunto = {"arroz", "feijão", "batata"}
conjunto_frozen = frozenset({"feijão", "arroz", "ovo"})
booleano = True
bites = b'Hello'
byte_array = bytearray(5)
memory_view = memoryview(bytes(10))
nenhum = None

"""Definindo tipos de dados"""

# Podemos especificar o tipo de dados usando suas classes 

x = str("Hello World")
x = int(20)	
x = float(20.5)	
x = complex(1j)	
x = list(("apple", "banana", "cherry"))	
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age=36)	
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))	
x = bool(5)	
x = bytes(5)		
x = bytearray(5)	
x = memoryview(bytes(5))

"""
continua...
https://www.w3schools.com/python/python_numbers.asp
"""