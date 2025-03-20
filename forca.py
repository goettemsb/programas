import random

def sorteio():
    return random.choice([    "astro", "bussola", "relampago", "sombra", "petala", 
    "oceano", "labirinto", "tempestade", "fossil", "vortice", 
    "brisa", "ecosistema", "serenidade", "misterioso", "enigma", 
    "constelacao", "silhueta", "vertigem", "quimera", "infinito"])


def forca(vidas):
    if vidas == 6:
        print("""
         ------
         |    |
         |    
         |    
         |    
         |
        =========
        """)
    elif vidas == 5:
        print("""
         ------
         |    |
         |    O
         |    
         |    
         |
        =========
        """)
    elif vidas == 4:
        print("""
         ------
         |    |
         |    O
         |    |
         |    
         |
        =========
        """)
    elif vidas == 3:
        print("""
         ------
         |    |
         |    O
         |   /|
         |    
         |
        =========
        """)
    elif vidas == 2:
        print("""
         ------
         |    |
         |    O
         |   /|\\
         |    
         |
        =========
        """)
    elif vidas == 1:
        print("""
         ------
         |    |
         |    O
         |   /|\\
         |   / 
         |
        =========
        """)
    elif vidas == 0:
        print("""
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |
        =========
        """)

palavra = sorteio() ##sorteio da palavra
print(palavra) ##teste

tam = len(palavra)
adivinhada = "_" * tam ##letras adivinhadas
vidas = 6
letras = "" ##letras já escolhidas
print(adivinhada) ##teste

jogoAtivo = True
while jogoAtivo:
    print()
    forca(vidas)
    print()
    print(adivinhada)
    print()
    print(f"Letras já escolhidas: {letras}")

    valida = False
    while not valida:
        letra = (input("Escolha uma letra:"))
        if letra not in letras: ##verifica se a letra escolhida está nas letras já digitadas
            valida = True
        else:
            print("letra já escolhida!")
    letras += letra ## registra letra digitada
    if letra in palavra:
        for pos in range(tam):
            if letra == palavra[pos]:
                adivinhada = adivinhada[:pos] + letra + adivinhada[pos+1:]

        
    else:
        print("letra não está na palavra")
        vidas = vidas - 1
        if vidas == 0:
            forca(vidas)
            print("voce perdeu")
            jogoAtivo = False

    if "_" not in adivinhada:
        print("Voce Ganhou!!!")
        jogoAtivo = False

print(f"Palavra sorteada era: {palavra}")


    
        


