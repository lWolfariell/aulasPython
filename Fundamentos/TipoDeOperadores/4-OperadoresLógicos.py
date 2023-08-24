""" O que são? """
""" 
São operadores utilizados em conjuntos com os operadores de comparação, para montar um expressão lógica. Quando um operador de comparação é utilizado, o resultado retornado é um booleano dessa forma
podemos combinar operadores de comparação com os operadores lógicos, exemplo:

op_comparacao + op_logico + op_comparacao...N...
 """

""" Exemplo """
saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite
#False
saldo >= saque or saque <= limite
#True

""" Operador Negação """

contatos_emergencia = []

not 1000 > 1500
#True
not contatos_emergencia
#True
not "saque 1500;"
#False
not ""
#True

""" Parênteses """
conta_especial = True

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
#True