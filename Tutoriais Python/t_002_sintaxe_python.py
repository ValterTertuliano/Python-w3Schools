"""Executando a sintaxe python"""

# como foi observado anteriormente podemos executar o codigo 
# diretamente na linha de comando, ou criando um arquivo .py 
# e executando ele na linha de comando

"""Indentação no Python"""

# No python a indentação é obrigatoria, em outras linguagens 
# os blocos geralmente são iniciados com {}, mas no python 
# ":" definem o bloco de codigo.

# exemplo:
if 5 > 2: # iniciamos um bloco condicional
    print("5 é maior que 2 !") # os espaços marcam o bloco

# ao contrario de outras linguagens não precisamos da chave 
# de fechamento para encerrar o fim do bloco, basta apenas 
# voltar o recuo
print("Saimos do bloco")

# não descomentar esse exemplo, gera erro de IndentationError
# if 5 > 2:
# print("5 é maior que 2") como não teve recuo ocorre um erro

# o uso de espaços fica a criterio, deve ter pelo menos um, 
# mas por convenção se utilizam 4 espaços (tab), porem cada 
# bloco deve ter a mesma quantia de espaços

"""Variáveis Python"""

# Variaveis são criadas a partir do momento que atribuimos um 
# valor a elas, o python não tem um comando para declarar 
# variaveis