cont = 0
soma_temp = 0
maior = -9999
menor = 9999
escaldantes = 0
mes_menor = 0
mes_maior = 0
mes_maior_texto = ""
mes_menor_texto = ""


for cont in range(12):
        while True:
            mes = int(input("\nDigite o número do mes: ")) ##\n para melhor visuaziliação
            if 1 <= mes <= 12:
                break  ##incrementa o contador somente quando for digitado um valor válido
            print("Valor Invalido, Digite um número entre 1 e 12.")

        while True:
            temp = float(input("Digite a temperatura do mes em Celsius: "))
            if -60 <= temp <= 50:
                break  ##incrementa o contador somente quando for digitado um valor válido

            print("Valor Invalido, digite um valor entre -60 e +50 ºC.")  
        
        soma_temp = soma_temp + temp ## Adiciona as temperaturas digitadas em uma variável (soma_temp), acumulador, para depois tirar a média
        if temp > maior: ## compara a temperatura digitada com a variável para definir o mes com maior temperatura
            maior = temp
            mes_maior = mes ## varíal mes_maior guarda o valor do mes digitado
        if temp > 33:
            escaldantes = escaldantes + 1 ## Escadantes recebe as temperaturas maiores que 33ºC
        if temp < menor: ## variável menor vai registrar sempre que o valor da temp digitada vai ser menor que o anterior
            menor = temp
            mes_menor = mes




media_temp = soma_temp/12 ##tira a média das temperaturas que foram somadas conforme linha 26 do código

if mes_maior == 1:
    mes_maior_texto = "Janeiro"
elif mes_maior == 2:
    mes_maior_texto = "Fevereiro"
elif mes_maior == 3:
    mes_maior_texto = "Março"
elif mes_maior == 4:
    mes_maior_texto = "Abril"
elif mes_maior == 5:
    mes_maior_texto = "Maio"
elif mes_maior == 6:
    mes_maior_texto = "Junho"
elif mes_maior == 7:
    mes_maior_texto = "Julho"
elif mes_maior == 8:
    mes_maior_texto = "Agosto"
elif mes_maior == 9:
    mes_maior_texto = "Setembro"
elif mes_maior == 10:
    mes_maior_texto = "Outubro"
elif mes_maior == 11:
    mes_maior_texto = "Novembro"
elif mes_maior == 12:
    mes_maior_texto = "Dezembro"

if mes_menor == 1:
    mes_menor_texto = "Janeiro"
elif mes_menor == 2:
    mes_menor_texto = "Fevereiro"
elif mes_menor == 3:
    mes_menor_texto = "Março"
elif mes_menor == 4:
    mes_menor_texto = "Abril"
elif mes_menor == 5:
    mes_menor_texto = "Maio"
elif mes_menor == 6:
    mes_menor_texto = "Junho"
elif mes_menor == 7:
    mes_menor_texto = "Julho"
elif mes_menor == 8:
    mes_menor_texto = "Agosto"
elif mes_menor == 9:
    mes_menor_texto = "Setembro"
elif mes_menor == 10:
    mes_menor_texto = "Outubro"
elif mes_menor == 11:
    mes_menor_texto = "Novembro"
elif mes_menor == 12:
    mes_menor_texto = "Dezembro"

##resultados conforme pede o enunciado
print(f"Média temperatura: {media_temp:.1f} ºC")
print(f"Maior temperatura: {maior:.1f} ºC no mes de {mes_maior_texto}")
print(f"Menor temperatura: {menor:.1f} ºC no mes de {mes_menor_texto}")
print(f"Qtde mses com temperatura maior que 33 ºc: {escaldantes}")




