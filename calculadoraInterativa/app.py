titulo = 'Calculadora Interativa'.center(90, '#')
print(titulo)

while True:
    valor1 = float(input('Entre com um valor\n'))
    operador = (input('Qual operador deseja usar: (+, - , *, /):\n'))
    valor2 = float(input('Entre com o segundo valor\n'))

    if operador == '+':
        resultado = valor1 + valor2
    elif operador == '-':
        resultado = valor1 - valor2
    elif operador == '*':
        resultado = valor1 * valor2
    elif operador == '/':
        if valor2 != 0:
            resultado = valor1 / valor2
        else:
            print('Não é possivel dividir por 0.')
            continue #reinicia o loop
    
    print('Resultado:', resultado)
    recomecar = input('Deseja recomeçar a operação? (s/n): ')
    if recomecar.lower() != 's':
        break