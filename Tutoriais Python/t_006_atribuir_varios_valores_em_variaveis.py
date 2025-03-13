"""Muitos valores para multiplas variaveis"""

# É permitido atribuir muitos valores a muitas variaveis em 
# uma linha, porem o numero dee variaveis deve ser igual ao 
# numero de valores atribuidos

x, y, z = 1, 2, 3
print(z, y, x) # saida 3 2 1

# Também é possivel atribuir um mesmo valor a varias variaveis
a = b = c = 5
print(a, b, c) # saida 5 5 5

""" Descompactando uma coleção"""

# se temos uma coleção com varios valores, podemos extrair 
# esses valores em variaveis, isso é chamado de "unpacking" 
# (descompactar)

numeros = [1, 2, 3]
um, dois, tres = numeros
print(um, dois, tres) # saida 1 2 3