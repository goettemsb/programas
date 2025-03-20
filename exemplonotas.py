import random

lista =[]
for i in range(1,15):
    lista.append(random.randint(1,100)/10)
print("Notas: ", lista)
media = sum(lista)/len(lista)

print("Media: ", media)

acima = 0
abaixo = 0

for nota in lista:
    if nota > media: acima = acima + 1
    if nota < media: abaixo = abaixo + 1

print("Qtde notas acima da média: ", acima)
print("Qtde notas abaixo da média: ", abaixo)
print("Qtde notas iguais média: ", lista.count(media))
print("Nota + alta", max(lista))
print("Nota + baixa", min(lista))

