import random
lista = []

for i in range (1,150): ## lista 24 notas
    lista.append(random.randint(1,6)) ## nota de 1 a 5
print("Notas: ", lista)

conceito = []
quantidade = []

conceito.append("Excelente")
quantidade.append(lista.count(5))
conceito.append("Bom")
quantidade.append(lista.count(4))
conceito.append("Regular")
quantidade.append(lista.count(3))
conceito.append("Ruim")
quantidade.append(lista.count(2))
conceito.append("Péssimo")
quantidade.append(lista.count(1))

maiorquantidade = quantidade[0]
maiorconceito = conceito[0]

for i in range (0,5):
    print(conceito[i]," - ", quantidade[i])
    if quantidade[i] > maiorquantidade:
        maiorquantidade = quantidade[i]
        maiorconceito = conceito [i]


print("Conceito mais votado: ", maiorconceito)
print("Recebeu ", maiorquantidade, " votos")




