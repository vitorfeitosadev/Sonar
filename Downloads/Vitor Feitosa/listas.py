frutas = ["banana", "laranja", "mamao"]
frutas1 = "banana"
frutas2 = "laranja"
frutas3 = "mamao"
frutas.sort()

''' é muito melhor escrever na forma de listas do que diversas variáveis, para fins de processamento e melhor aproveitamento do sistema.'''

frutas.remove(frutas[1])
frutas.append(input("Qual fruta gostaria de inserir ? "))
print(frutas)
print(len(frutas))

'''Método len (lenght) para entender o cumprimento de uma lista (array), ou seja, quantos itens aquela variável possui'''
'''Métdo append adiciona itens a lista // método remove, faz o obvio, remove itens da lista'''


