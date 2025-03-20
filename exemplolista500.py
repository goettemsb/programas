import random

lista = []
for i in range (1,7):
    lista.append(random.randint(1,61))
print(lista)

maior = lista[0]
pares = 0
for num in lista:
    if num > maior: maior = num
    if num%2==0: pares = pares + 1

print("Maior: ", maior)
print("Qtde Pares: ", pares)



