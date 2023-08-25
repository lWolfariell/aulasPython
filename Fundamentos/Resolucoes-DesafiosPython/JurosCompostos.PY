valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final = valor_inicial

## Iterar, baseado no período em anos, para calculo do valorFinal com os juros.

#M = C ( 1+i)t
#5000 = C (1+0.08)5

juros_compostos = valor_inicial * (1+taxa_juros)**periodo

valor_final = juros_compostos

print(f"Valor final do investimento: R$ {valor_final:.2f}")