""" O que são? """
""" São operadores utilizados para compara se os dois objetos testados ocupam a mesma posição na memória """
""" Exemplo """
curso = 'Curso de Python'
nome_curso = curso
saldo, limite = 200, 300

curso is nome_curso
#True

curso is not nome_curso
#False

saldo is limite
#True