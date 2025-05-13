lista = []
comando = int(input(
    "Escolha uma das opções: \n1. Inserir item a lista.\n2. Ver a lista. \n3. Apagar um item da lista.\n4. sair.\nInsira o numero: "))

while comando != 4:
    if comando == 1:
        item = input("Insira o item: ")
        lista.append(item)
        print("")
        comando = int(input("O que fazer a seguir: \n1. Inserir item a lista.\n2. Ver a lista. \n3. Apagar um item da lista.\n4. sair.\nInsira o numero: "))
    elif comando == 2:
        for i in range(len(lista)):
            print(lista[i], end=" ")
            print("")
        comando = int(input("O que fazer a seguir: \n1. Inserir item a lista.\n2. Ver a lista. \n3. Apagar um item da lista.\n4. sair.\nInsira o numero: "))

    elif comando == 3:
        for i in range(len(lista)):
            print([i], lista[i])
        apagarItem = int(input("Digite o número do item que quer apagar: "))
        lista.pop(apagarItem)
        comando = int(input("O que fazer a seguir: \n1. Inserir item a lista.\n2. Ver a lista. \n3. Apagar um item da lista.\n4. sair.\nInsira o numero: "))
