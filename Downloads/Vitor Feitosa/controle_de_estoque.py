# nomes = []
# quantidades = []
def controle_de_estoque(nomes, quantidades):
    estoque_menorque5 = []
    estoque_0 = []

    for i in range(len(nomes)):
        if quantidades[i] == 0:
            estoque_0.append(nomes[i])
        elif quantidades[i] < 5:
            estoque_menorque5.append(nomes[i])

    print("Produtos com estoque menor que 5:")
    for i in estoque_menorque5:
        print(f'-> {i}')

    print("Produtos com estoque nulo: (Fazer pedido urgente!)")
    for i in estoque_0:
        print(f'-> {i}')
        