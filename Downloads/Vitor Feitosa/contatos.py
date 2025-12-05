def encontrar_posicao_loop(lista, item):
    """
    Encontra a posição usando um loop.
    """
    for indice, elemento in enumerate(lista):
        if elemento == item:
            return indice
    return -1

# Exemplo
frutas = ['maçã', 'banana', 'laranja', 'uva']
print(encontrar_posicao_loop(frutas, 'laranja'))