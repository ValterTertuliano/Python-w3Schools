"""String Concatenação"""

# Concatenar é combinar duas ou mais strings e podemos fazer 
# isso com o operador +

# Exemplo
a = "Meu Nome é "
b = "Valter Tertuliano"
c = a + b
print(c) # Meu Nome é Valter Tertuliano

# devemos tomar cuidado com espaços, no exemplo anterior a 
# variavel 'a' tem um espaço extra no fim da string, em casos 
# que isso não for possivel podemos fazer da seguinte forma

d = "oi"
e = "tudo bem?"
f = d + e
print(f) # Saída: oitudo bem?
g = d + " " + e
print(g) # Saída: oi tudo bem?