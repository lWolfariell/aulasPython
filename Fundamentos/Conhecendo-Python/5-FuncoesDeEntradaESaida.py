""" Função input (buuilt-in) / função de entrada"""
""" Essa função é utilizada quando queremos ler dados de entrada padrão(teclado). Independente o valor que é inserido essa função sempre lerá como STRING """

""" Função print (built-in) / função de saida """
""" é utilizada quando queremos exibir dados na saida padrão (tela) """

nome = input ('Informe o seu nome: ')
idade = input ('Informe a sua idade: ')

print(nome, idade)
print(nome, idade, end='...\n')
print(nome, idade, sep='#')
