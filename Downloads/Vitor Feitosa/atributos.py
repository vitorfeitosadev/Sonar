contatos = [
    {"nome": "gostosinha", "telefone": 666},
    {"nome": "stevie", "telefone": 123123},
    {"nome": "yaheafad", "telefone": 312321}
]
#print(contatos[0])

def add_contato(nome, telefone):
    contatos.append({"nome": nome, "telefone": telefone})
    print(f'{nome} foi adicionado a lista de contatos')

def busca_contato(nome):
    for i in contatos:
        if nome.lower()== i["nome"]:
            return i
        else:
            return None

def atualizar_contato(nome, novo_telefone):
    contato = busca_contato(nome)
    if contato:
        contato["telefone"] = novo_telefone
    else:
        print('Contato não encontrado')

def encontrar_posicao_loop(lista, item):
 
    for indice, elemento in enumerate(lista):
        if elemento == item:
            return indice
    return -1
    
    
        
#Definir uma função apenas como um valor, ou como um método, caso você inclua os 2 gera divergências, devido a ambiguidade.

#No caso de duas entradas com o mesmo nome, deve-se aprimorar o código para que tenha um novo paramêtro de pesquisa


add_contato("Joao", 3123123)

print(busca_contato("Gostosinha"))

#MENU DE REMOÇÂO
print("Bem vindo a agenda telefonica")
while True:
    opcao = input("Seleciona uma opção \n -> 1 Adicionar contato \n -> 2 para buscar um contato \n -> 3 Atualizar Contato \n -> 4 Remover contato: \n 5 Sair: ")
    if opcao == "1":
        add_contato((input("o nome que deseja adicionar:")), int(input("Digite o número que deseja adicionar:")))
    elif opcao == "2":
        contato_encontrado = busca_contato(input('Digite o nome do contato que deseja buscar na agenda: '))
        print(f'O numero de {contato_encontrado["nome"]} é {contato_encontrado["telefone"]}')
    elif opcao == "3":
        contato_encontrado = busca_contato(input('Digite o nome do contato que deseja buscar na agenda: '))
        novo_contato = [contato_encontrado.index] = add_contato(input('Digite o nome que deseja adicionar: '), int(input('Digite o número do contato que deseja adicionar: ')))
    elif opcao == "4":
        for i in contatos:
            print(f'Contato: {i['nome']} \n Telefone: {i['Telefone']} \n')
    elif opcao == "5":
        break

encontrar_posicao_loop(contatos, input('Digite o nome que deseja remover: ').lower()== i["nome"])



