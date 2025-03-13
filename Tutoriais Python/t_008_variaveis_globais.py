"""Variaveis globais"""

# Variaveis criadas foras de uma função, são conhecidas como 
# variaveis globais, elas podem ser usadas tanto dentro 
# quanto fora das funções e por qualquer outro arquivo/pessoa

# exemplo
variavel = "Incrivel"
def umaFuncao():
    print("Python é " + variavel)
umaFuncao() # vai exibir Python é Incrivel

# Se for criada uma variavel dentro da função com o mesmo 
# nome da variavel que esteja fora dela, essa variavel será 
# uma variavel local dentro da função, e a função vai usar a 
# variavel local, a variavel fora do escopo da função vai se 
# manter com seu valor original e sem alteração

# exemplo
variavel1 = "Valter"
def umaOutraFuncao():
    variavel1 = "Sergio"
    print("Meu nome é " + variavel1)

umaOutraFuncao() # saida: Meu nome é Sergio
print("Meu nome é " + variavel1) # saida: Meu nome é Valter

"""Palara-chave Global"""

# Podemo usar a palavra chave global em uma variavel dentro 
# de uma função essa variavel se torna de uso global, e se 
# houver uma variavel fora do escopo da função, essa variavel 
# é modificada com o uso da palavra-chave global

# exemplo
var2 = "RIBEIRO"
def outra_funcao():
    global var # criando uma variavel global
    global var2 # modificando a variavel global
    var = 'Tertuliano'
    var2 = "Ribeiro"

outra_funcao() # com a chamada da função criamos a variavel global
print("Meu nome é Valter Sergio " + var2 + " " + var)


"""
https://www.w3schools.com/python/python_datatypes.asp
"""
