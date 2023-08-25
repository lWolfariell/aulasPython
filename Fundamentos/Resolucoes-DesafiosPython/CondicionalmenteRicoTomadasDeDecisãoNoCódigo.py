# - Cada cliente digitará o valor do seu saldoTotal de sua conta bancária e o valorSaque.
saldo_total = int(input())
valor_saque = int(input())

#Regras do saque:

# - Um saque só pode ser realizado se o saldoDisponível na conta for igual ou superior ao valor solicitado.

saldoDisponivel = saldo_total - valor_saque

# - Se o saldo for suficiente, o valor solicitado deve ser subtraído do saldo disponível, indicando que o saque foi realizado.
if saldoDisponivel >= 0:
    saldo_total = saldoDisponivel
    print(f'Saque realizado com sucesso! Novo saldo: {saldo_total}')
    # - Se o saldo for insuficiente, o saque não deve ser realizado e uma mensagem adequada deve ser exibida.
else:
    print('Saldo insuficiente. Saque nao realizado!')

