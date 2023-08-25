ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input())

# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)
    
lista_ordenadas = sorted(ativos)

for itemOrdenado in lista_ordenadas:
    print(itemOrdenado)