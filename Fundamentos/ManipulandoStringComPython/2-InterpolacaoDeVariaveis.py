""" Método format """

nome = 'Vitor Guilherme'
idade = 28
profissao = 'Desenvolvedor Front End'
linguagem = 'Python'

print('Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}\n'.format(nome, idade, profissao, linguagem))

print('Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}\n'.format(linguagem,  profissao, idade, nome))

print('Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}\n'.format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

#print('Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}\n'.format(**pessoa))

""" Método f-string """

print(f'Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}\n')

""" Formatar string com f-string """
#Nesse exemplo formatar com até duas casas decimais

PI = 3.14159

print(f'Valor de PI: {PI:.2f}') #Sintaxe (variavel:.numeroDeEspaçoDesejadof)
#Valor de PI: 3.14

print(f'Valor de PI: {PI:10.2f}')#aqui foi definido 10 caracteres de espaços
#Valor de PI:          3.14
