class Pizza:
    def __init__(self, nome, ingredientes, preco):
        self.nome = nome
        self.ingredientes = ingredientes
        self.preco = preco
    
    def  __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"
    

class Pedido:
    def __init__(self, cliente, endereco):
        self.cliente = cliente
        self.endereco = endereco
        self.pizzas = []
        self.__total = 0.0
        self.__status = "preparando"

    def get_total(self):
        return self.__total
    
    def get_status(self):
        return self.__status

    def adicionar_pizza(self, pizza):
        self.pizzas.append(pizza)
        self.__total += pizza.preco

    def finalizar_pedido(self):
        if len(self.pizzas) > 0:
            self.__status = "a caminho"
            return True
        return False

    def exibir_resumo(self):
        print(f'Cliente: {self.cliente}\nEndereço: {self.endereco}\nStatus: {self.get_status()}\nTotal do Pedido: {self.get_total()}')
        for i in self.pizzas:
            print(i.__str__())

def main():
    cardapio = [
    Pizza("Mussarela", ["Molho", "Queijo", "Orégano"], 30.00),
    Pizza("Calabresa", ["Molho", "Queijo", "Calabresa", "Cebola"], 35.00),
    Pizza("Frango Catupiry", ["Molho", "Queijo", "Frango", "Catupiry"], 40.00),
    Pizza("Portuguesa", ["Molho", "Queijo", "Presunto", "Ovo", "Cebola"], 38.00)
    ]

    pedido_atual = None
    print("="*30 + "\nBEM-VINDO AO SISTEMA JWC PIZZA\n" + "="*30)

    while True:
        opcao = input("\n--- MENU PRINCIPAL ---\n1. Iniciar Novo Pedido\n2. Ver Cardápio\n3. Adicionar Pizza ao Pedido\n4. Ver Resumo do Pedido\n5. Finalizar Pedido\n0. Sair do Sistema\n\nDigite sua escolha: ")
        if opcao == "1":
            pedido_atual = Pedido(input("Digite o seu nome: "), input("Digite o seu endereço: "))
        elif opcao == "2":
            for i in cardapio:
                print(i.__str__())
        elif opcao == "3":
            if pedido_atual != None:
                index = 1
                for i in cardapio:
                    print(f'{index}. {i.__str__()}')
                    index +=1
                pedido_atual.pizzas.append(cardapio[int(input("Digite o número da Pizza escolhida: ")) - 1])
            else:
                print("Inicie o seu pedido primeiro.")
        elif opcao == "4":
            if pedido_atual != None:
                pedido_atual.exibir_resumo()
            else:
                print("Inicie o seu pedido primeiro.")
        elif opcao == "5":
            if pedido_atual != None:
                pedido_atual.finalizar_pedido()
            else:
                print("Inicie o seu pedido primeiro.")
        elif opcao == "0":
            break
        else:
            print("Opção inválida, tente novamente.")
main()