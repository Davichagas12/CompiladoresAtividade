import requests

fontemoedas = requests.get("https://free.currconv.com/api/v7/currencies?apiKey=4f0ca69d0747e3d4c624").json()
moedas = list(fontemoedas['results'].keys())

print("Bem vindo ao Câmbio de Moedas")
while True:
    print("Escolha uma opção:")
    print("-> 1 - Listar todas as moedas disponíveis")
    print("-> 2 - Converter valor para outra moeda")
    print("-> 3 - Cotação da moeda")
    print("-> 4 - Sair")

    try:
        escolhausuario = int(input())
    except:
        print("Escolha inválida")
        break

    if escolhausuario == 1:
        print(moedas)

    elif escolhausuario == 2:
        try:
            print("Insira a moeda inicial:")
            moedaInicial = input().upper()
            if moedaInicial not in moedas:
                raise Exception

            print("insira o valor a ser convertido: ")
            valorInicial = int(input())


            print("Inserir a moeda final:")
            moedaConvertida = input().upper()
            if moedaConvertida not in moedas:
                raise Exception

            Id = moedaInicial + "_" + moedaConvertida
            resp = requests.get("http://free.currconv.com/api/v7/convert?apiKey=4f0ca69d0747e3d4c624&q=" + Id + "&compact=ultra").json()
            taxa = resp[Id]
            valorFinal = valorInicial * taxa
            print("1 " + moedaInicial + " = " +  str(taxa) + " " + moedaConvertida)
            print(str(valorInicial) + " " + moedaInicial + " = " +  str(valorFinal) + " " + moedaConvertida)

            data = open(Id + ".csv", "w+")
            novoCambio = str(valorInicial) + ";" + moedaInicial + ";" + str(valorFinal) + ";" + moedaConvertida
            data.write(novoCambio)
            data.close()

            print("Deseja continuar? (S/N):")
            if input().upper() == "N":
                break
        except:
            print("Valor inválido")

    elif escolhausuario == 3:
        try:
            print("Insira a moeda inicial:")
            moedaInicial = input().upper()
            if moedaInicial not in moedas:
                raise Exception

            print("Insira a moeda final:")
            moedaConvertida = input().upper()
            if moedaConvertida not in moedas:
                raise Exception

            Id = moedaInicial + "_" + moedaConvertida
            resp = requests.get("http://free.currconv.com/api/v7/convert?apiKey=4f0ca69d0747e3d4c624&q=" + Id + "&compact=ultra").json()
            valorconvertido = resp[Id]
            print("1 " + moedaInicial + " = " +  str(valorconvertido) + " " + moedaConvertida)

            data = open(Id + ".csv", "w+")
            novoCambio = moedaInicial + "," + str(valorconvertido) + "," + moedaConvertida
            data.write(novoCambio)
            data.close()

            print("Deseja continuar? (S/N):")
            if input().upper() == "N":
                break
        except:
            print("Valor inválido")
    elif escolhausuario == 4:
        break
    else:
        print("Escolha inválida")
        break


