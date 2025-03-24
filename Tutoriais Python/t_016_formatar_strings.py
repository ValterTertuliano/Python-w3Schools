""""Formatar Strings"""

# Não podemos concatenar strings com tipos diferentes de 
# dados, para isso podemos usar 'f-strings' ou o método 
# 'format()'.

# Para usar 'f-strings' para realizar interpolações, devemos 
# usar a letra 'f' minuscula antes das aspas, e, adicionar 
# chaves para formatar a string adicionando variaveis ou 
# realizar operações diretamente ' f"{Valor a ser formatado, 
# ou substituido}" '

# Exemplo: 
num = 30
# print("O número " + num) # Saída: TypeError -> não pode concatenar str com int
print(f'O número {num}') # Saída: O número 30

# podemos realizar operações diretas
print(f'A soma de {num} + {5} é {num + 5 }') # Saida: A soma de 30 + 5 é 35
