"""Conversão de tipo"""

# Como visto anteriormente podemos especificar um tipo de 
# dado, em python podemos usar casting, usando classes de 
# tipo de dados para modificar dados

# Regras de conversão 

# int() - constrói um número inteiro a partir de um literal 
# inteiro, um literal float (removendo todos os decimais) ou 
# um literal de string (desde que a string represente um 
# número inteiro)

# float() - constrói um número float a partir de um literal 
# inteiro, um literal float ou um literal de string (desde 
# que a string represente um float ou um inteiro)

# str() - constrói uma string a partir de uma ampla variedade 
# de tipos de dados, incluindo strings, literais inteiros e 
# literais float

# Exemplo int:
x = int(1)   # Saída: 1
y = int(2.8) # Saída: 2
z = int("3") # Saída: 3

# Exemplo float:
x = float(1) # Saída: 1.0
y = float(2.8) # Saída: 2.8
z = float("3") # Saída: 3.0
w = float("4.2") # Saída: 4.2

# Exemplo string(literais de texto)
x = str("s1") # Saída: 's1'
y = str(2) # Saída: '2'
z = str(3.0) # Saída: '3.0'
