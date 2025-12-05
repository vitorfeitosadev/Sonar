def lista_compras():
    lista = []
    produto = ""  

    while True:
        produto = input("Digite o produto ou 'fim' para sair:\n-> ")
        if produto.lower() == "fim":
            break

        # Verifica se o produto já está na lista
        encontrado = False
        for item in lista:
            if item["nome"].lower() == produto.lower():
                item["quantidade"] += 1
                encontrado = True
                break
        if not encontrado:
            lista.append({"nome": produto, "quantidade": 1})

    # Ordena a lista original diretamente (não cria uma cópia).
    # O parâmetro key define o critério da ordenação:
    #   - para cada item (x), que é um dicionário,
    #   - pegamos o valor da chave 'nome'
    #   - transformamos em minúsculas (.lower()) para que
    #     "Banana" e "banana" fiquem na mesma ordem correta.
    lista.sort(key=lambda x: x["nome"].lower())

    print("\nLista de compras (sem repetições):")
    for item in lista:
        print(f"{item['nome']} (Quantidade: {item['quantidade']})")

    print(f"\nTotal de itens diferentes: {len(lista)}")

lista_compras()
