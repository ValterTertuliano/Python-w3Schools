"Strings em Python"

# Strings(Textos) podem ser cercadas por aspas duplas("") ou 
# simples('')

# Exemplo:
print('Olá mundo !!!')
print("Olá mundo !!!")

"Citações dentro de citações"
# Podemos fazer citações com aspas dentro de strings desde 
# que as aspas inicias sejam diferentes do texto citado

# Exemplo:
print("Meu nome é 'Valter'.") # Saida: Meu nome é 'Valter'.
print('Meu nome é "Valter".') # Saida: Meu nome é "Valter".

"Strings multilinhas"
# Podemos escrever um texto com varias linhas usando 3 aspas 
# consecutivas, tanto com aspas duplas ou simples

# Exemplo:
print("""Texto linha 1,
texto linha 2,
texto linha 3""")

"Strings são matrizes"

# Strings em Python são matrizes de bytes que representam 
# caracteres Unicode. Entretanto, Python não tem um tipo de 
# dado de caractere, um único caractere é simplesmente uma 
# string com comprimento 1, colchetes podem ser usados ​​para 
# acessar elementos da string

# Exemplo:
texto = 'Boa tarde'
print(texto[0]) # Saída: B

"Loop em strings"

# Como strings são matrizes podemos realizar loops para 
# percorrer cada caracter em uma string

# Exemplo:
for x in "Tertuliano":
    print(x)

"Comprimento de uma string"

# As vezes é necessário obter o tamanho de uma string e a 
# função 'len()' retorna a quantia exata de caracteres

# Exemplo:
print(len("abc")) # Saida: 3 

# Podemos verificar se uma determinada frase ou caractere 
# está presente em uma string usando a palavra chave 'in', 
# ou, usando condicionais, operadores de negação e etc.

# Exemplo:
txt = "Me chamo Valter e estudo Python"
print("estudo" in txt) # Saida: True

print("SIM" if "valter" in txt else "NÃO") # Saída: Não --> valter com letra minuscula 

