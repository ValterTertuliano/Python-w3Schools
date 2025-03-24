"""Modificar strings"""

# Existem varios métodos integrados para modificar strings, 
# string é um objeto da classe string.

"Maiúsculas e minúsculas"

# Podemos usar os métodos 'upper()' e 'lower()' para garantir 
# que todos os caracteres de uma string estejam em um mesmo 
# padrão de formato

# Exemplo:
print("OLÁ".lower()) # Saída: olá
print("olá".upper()) # Saída: OLÁ

# Podemos remover todos os espaços em branco extra tanto no 
# inicio quanto no final usando o método 'strip()'.
palavra = "     removendo espaços   "
print(palavra.strip() + '.') # Saída: removendo espaços.

# Podemos substituir caracteres de uma string por outros 
# caracteres usando o método 'replace()'
print("abracadabra".replace("a", "o")) # Saída: obrocodobro

# teste aleatorio da cabeça
cpf = '123456789-12'
ocultar_cpf = []
for x in cpf:
    if x == '-':
        ocultar_cpf.append(x)
    else:
        ocultar_cpf.append(x.replace(x, 'x'))
    
print("".join(ocultar_cpf)) # Saída: xxxxxxxxx-xx

# Melhorando o teste
rg = '123456789-01'
ocultar_rg = []
for x in rg:
    ocultar_rg.append('x' if x != '-' else '-')
print("".join(ocultar_rg)) # Saída: xxxxxxxxx-xx

# Podemos dividir uma string em substrings usando o método 
# 'split()' tendo como retorno uma lista

# Exemplo:

# Sem paramentros ele quebra todos os espaços em branco
print("abc do        tio".split()) # Saída: ['abc', 'do', 'tio']

# Com parametros podemos definir o separador
print("abc do tio valter".split('o')) # Saída: ['abc d', ' ti', ' valter']

