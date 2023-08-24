""" entradas = [7, -5, 6, -3.4, 4.6, 12]

numeros_positivos = []
soma_positivos = 0

for entrada in entradas:
    if entrada > 0:
        numeros_positivos.append(entrada)
        soma_positivos += entrada

quantidade_positivos = len(numeros_positivos)
media = soma_positivos / quantidade_positivos

 
print(f'{quantidade_positivos} valores positivos')

print(media) """

count=0
sum=0.0
for i in range(1,7):
    n = float(input())
    if(n>0):
        sum = sum + n
        count=count+1
print("{} valores positivos".format(count))
print("%0.1f"%(sum/count))