valor = float(input())
saldo = 0

if valor > 0:
    #Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
    saldo += valor
    print(f'Deposito realizado com sucesso!\nSaldo atual: R$ {saldo:.2f}')
elif valor < 0:
   #Imprimir a mensagem de valor inválido.
   print('Valor invalido! Digite um valor maior que zero.')
else:
  #Imprimir a mensagem de encerrar o programa.
  print('Encerrando o programa...')