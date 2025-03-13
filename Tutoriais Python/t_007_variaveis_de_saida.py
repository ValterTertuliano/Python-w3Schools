"""Variaveis de saida"""

# a função print() é usada para exibir os valores de uma 
# variavel, no caso de varias variaveis devemos separar eles 
# por virgula, podemos usar o operador "+" para concatenar 
# strings ou realizar operações matematicas com tipos 
# numericos, a função print() tem um parametro chamado end 
# que define como a função vai finalizar seus valores, e o 
# parametro sep que define os separadores de cada valor

x = 'Olá'
y = 'Mundo'
z = '!!!'

# por padrão o separador é um espaço em branco
# por padrão o end é um \n ou seja pula uma linha
print(x, y, z)  # saida Olá Mundo !!!

# exemplo com separador definido como * e o end um espaço 
# vazio, o segundo print vai aparecer na mesma linha que o 
# primeiro

print(x, y, z, sep='*', end='') # saida: Olá*Mundo*!!!O end não pulou a linha
print("O end não pulou a linha ")

"""
onde parei e devo continuar
https://www.w3schools.com/python/python_variables_global.asp
"""
