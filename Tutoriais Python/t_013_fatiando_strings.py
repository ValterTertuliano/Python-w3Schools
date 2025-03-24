'''Fatiando strings'''

# Podemos pegar um pedaço de caracteres usando a sintaxe de 
# fatiamento, para isso devemos definir o índice inicial e 
# final, separando o inicio e o fim por dois pontos(:).

# Exemplo:
abc = "abcde"
print(abc[0:3]) # Saída: abc

# podemos ignorar o indice inicial se quiser pegar desde o 
# começo até certo limite
print(abc[:3]) # Saída: abc

# podemos ignorar a parte inicial da string deixando de fora 
# o índice final
print(abc[3:]) # Sáida de

"Indexação negativa"

# Podemos usar indices negativos para iniciar o fatiamento a 
# partir do final da string, quando usamos essa tecnica de 
# fatiamento o primeiro elemento de trás para frente é sempre 
# -1, por exemplo no texto 'abcde' -1 se refere a última 
# letra 'e', e o ultimo elemento das 5 letras é -5, ou seja 
# não contamos zero, já que com fatiamento normal o primeiro 
# valor é sempre indexado com 0, no caso dessa string 
# teriamos que fatiar com números positivos de 0 a 4.

# Exemplo:

# Último elemento
print(abc[-1:]) # Saída: e

# O primeiro elemento de trás para frente -5
# O segundo elemento de trás para fente -2
print(abc[-5:-2]) # Saída: abc