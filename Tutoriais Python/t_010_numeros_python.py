"""Números Python"""

# O python trabalha com 3 tipos numéricos, int, float e 
# complex

"""int"""
# São todos os números inteiros positivos e negativos
# Exemplo:
n1 = 1
n2 = -1

"""float"""
# São todos os números reais positivos e negativos, eles 
# também podem ser um número científico usando um "e" para 
# indicar uma potência de 10
# Exemplo:
n1 = 1.5
n2 = -1.5
n3 = 5e3

"""complex"""
# Números complexos são escritos com um 'j' como parte 
# imaginária
# Exemplo:
n1 = 1+1j
n2 = 5j
n3 = -5j

"Conversão de tipos"

# Podemos converter um tipo de número para outro usando suas 
# respectivas classes, com excessão dos números complexos que 
# não podem ser convertidos para outros tipo
# Exemplo int:
x = 1
x1 = float(1)
x2 = complex(x)
print(x1) # Saída: 1.0
print(x2) # Saída: (1+0j)

# Exemplo float:
y = 1.5
y1 = int(y)
y2 = complex(y)
print(y1) # Saída: 1
print(y2) # Saída: (1.5+0j)

"""Número aleatório"""

# O python tem uma biblioteca para gerar numeros aleatórios 
# chamada 'random', devemos importar a biblioteca e usar a 
# função 'randrange()', e também podemos usar a função 'random
# ()' para gerar numeros reais.
# Exemplo:
import random 
numero_aleatorio = random.randrange(1, 100)
print(numero_aleatorio) # um tipo inteiro entre zero a cem

numero_flutuante_aleatorio = random.random()
print(numero_flutuante_aleatorio)

