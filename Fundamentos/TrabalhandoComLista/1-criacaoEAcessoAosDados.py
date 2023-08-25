""" Criando listas """
""" Lista em Python pode armazenar de maneira sequencial qualquer tipo de objeto. Podemos criar lista utilizando o construtor list, a função range ou colocando valores separados por virugula dentro de colchetes.Listas são objetos mutáveis, portanto podemos alterar seus valores após a criação """

""" Exemplos """

frutas = ['laranja', 'maca', 'uva']

frutas = []

letras = list('python')
print(letras)

numeros = list(range(10))
print(numeros)

carro = ['Ferrari', 'F8', 4200000, 2020, 2900, 'São Paulo', True]

""" Acesso direto """
""" A lista é uma sequência, portanto podemos acessar seus dados utilizando índices. Contamos o índice de determinada sequencia a partir do zero """

""" Exemplo """
frutas[1] #maca
frutas[2] #uva

""" Indices negativos """
""" Exemplo """

frutas[-1] #uva
frutas[-2] #maca

""" listas aninhahda """

""" Exemplo """
matriz = [
    [1, 'a', 2],
    ['b', 3, 4],
    [6, 5, 'c']
]

matriz[0] # [1, 'a', 2]
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # 'c'

""" Fatiamento """
""" Alem de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequencia. Para isso basta passar o índice inicial e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursor deve 'pular no acesso """

lista = ['p', 'y', 't', 'h', 'o', 'n']

lista[2:] #['t', 'h', 'o', 'n']
lista[:2] #['p', 'y']
lista[1:3] #['y', 't']
lista[0:3:2] #['p','t']
lista[::] #['p', 'y', 't', 'h', 'o', 'n']
lista[::-1] #['n', 'o', 'h','t', 'y', 'p']

""" Compreensao de listas """
""" A compreensao de lista oferece uma sintaxe mais curta quando você deseja: criar uma nova lista com base nos valores de uma lista existente(filtro) ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente """

""" Filtro versão 1 """

numeros = [1, 30 , 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

""" Filtro Versao 2 """
numeros = [1, 30 , 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

""" Modificando valores versão 1 """
numeros = [1, 30 , 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

""" Modificando valores versão 2 """
numeros = [1, 30 , 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]