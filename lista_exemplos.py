lista2 = ["o", "menino", "jogou", "a", "bola"]

for item in lista2:
    print(item)


a = input("Digite uma palavra: ")


if a in lista2:
    print("{a} Está na lista")

elif a not in lista2:
    print("{a} não Está na lista")


