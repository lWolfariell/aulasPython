""" Metodos """

""" Maisculas , minúscula e titulo """
curso = 'pYtHon'

print(curso.upper())
#PYTHON

print(curso.lower())
#python

print(curso.title())
#Python

""" Eliminando espaços em branco """

curso = '    pyhton  '

print(curso.strip())
#Python

print(curso.lstrip())
#Python   '

print(curso.rstrip())

#   Python

""" Junções e centralização """

curso = 'Python'

print(curso.center(10, '#')) # determinado 10 caracteres que ele irá ocupar, o segundo argumento é opcional você informa o caracteres que irá ocupar
#'##Pyhton##'

print('.'.join(curso)) #Você define o que você quer juntar nesse caractere no exemplo foi usado o '.'
#'P.y.t.h.o.n'


