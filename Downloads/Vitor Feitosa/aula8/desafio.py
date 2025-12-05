class Item:
    def __init__(self, sku, nome, __peso, __quantidade):
        self.sku = sku
        self.nome = nome
        self.__peso = __peso
        self.__quantidade = __quantidade

    def get_peso(self):
        return self.__peso
    
    def get_quantidade(self):
        return self.__quantidade
    
    def dar_baixa_estoque(self, quantidade_a_remover):
        if self.__quantidade >= quantidade_a_remover:
            self.__quantidade -= quantidade_a_remover
            return True
        return False
    
class Pacote:
    def __init__(self, codigo_rastreio, endereco):
        self.codigo_rastreio = codigo_rastreio
        self.endereco = endereco
        self.itens = []
        self.__peso_total= 0.0
        self.__despachado = False

    def get_peso_total(self):
        return self.__peso_total
    
    def get_status(self):
        return self.__despachado
    
    def adicionar_item(self, item):
        self.itens.append(item)
        self.__peso_total += item.get_peso()

    def despachar(self):
        if self.itens:
            self.__despachado = True
            return True
        return False

class CentroDistribuicao:
    def __init__(self, nome):
        self.nome = nome
        self.inventario = {}
        self.pacotes = {}

    def _buscar_item(self, sku):
        return self.inventario.get(sku)
    
    def _buscar_pacote(self, codigo_rastreio): 
        return self.pacotes.get(codigo_rastreio)
    
    def cadastrar_item(self, sku, nome, peso, quantidade):
        if peso<=0 or quantidade<=0:
            print("Erro: Peso e quantidade devem ser positivos.")
            return False
        if self._buscar_item(sku):
            print("Erro: SKU já cadastrado.")
            return False
        self.inventario[sku] = Item(sku, nome, peso, quantidade)
        return True
    
    def criar_pacote(self, codigo_rastreio, endereco):
        if self._buscar_pacote(codigo_rastreio):
            print("Erro: Pacote já existe")
            return False
        self.pacotes[codigo_rastreio] = Pacote(codigo_rastreio, endereco)
        return True

    def adicionar_item_pacote(self, sku, codigo_rastreio):
        item_obj = self._buscar_item(sku)
        pacote_obj = self._buscar_pacote(codigo_rastreio)
        #if item_obj == None and pacote_obj == None:
            #print("Item e pacote não encontrados")
            #return False
        if item_obj == None:
            print("Item não encontrado")
            return False
        if pacote_obj == None:
            print("Pacote não encontrado")
            return False
        if pacote_obj.get_status() == "Despachado":
            print("Erro: Pacote já despachado.")
            return False
        sucesso_estoque = item_obj.dar_baixa_estoque(1)
        if sucesso_estoque == False:
            print("Erro: Item fora de estoque.")
            return False
        pacote_obj.adicionar_item(item_obj)
        return True
    
    def despachar_pacote(self, codigo_rastreio):
        pacote_obj = self._buscar_pacote(codigo_rastreio)
        if pacote_obj == None:
            print("Erro: Pacote não encontrado.")
            return False
        sucesso = pacote_obj.despachar()
        if sucesso == False:
            print("Erro: Pacote vazio.")
            return False
        print("Pacote despachado!")
        return True

    def ver_invetario(self):
        for i in self.inventario:
            print(f'SKU: {self.inventario[i].sku}\nNome: {self.inventario[i].nome}\nEstoque: {self.inventario[i].get_quantidade()}')

    def ver_pacotes(self):
        for i in self.pacotes:
            print(f'Código: {self.pacotes[i].codigo_rastreio}\nEndereço: {self.pacotes[i].endereco}\nStatus: {self.pacotes[i].get_status()}')

def main():
    centro = CentroDistribuicao("CD-RJ-01")
    print(f"--- Bem-vindo ao Sistema LogiRápida ({centro.nome}) ---")
    
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Cadastrar Novo Item no Inventário")
        print("2. Criar Novo Pacote")
        print("3. Adicionar Item a um Pacote")
        print("4. Despachar Pacote")
        print("5. Ver Inventário (Estoque)")
        print("6. Ver Pacotes (Status)")
        print("0. Sair")
        
        opcao = input("Digite sua escolha: ")

        if opcao == '0':
            print("Saindo do sistema...")
            break

        elif opcao == '1':
            print("\n[Opção 1: Cadastrar Item]")
            try:
                sku = input("Digite o SKU: ")
                nome = input("Digite o Nome: ") 
                peso_str = input("Digite o Peso (ex: 2.5): ")
                peso_float = float(peso_str) 
                qtd_str = input("Digite a Quantidade (ex: 10): ")
                qtd_int = int(qtd_str)
                
                sucesso = centro.cadastrar_item(sku, nome, peso_float, qtd_int)
                
                if sucesso: 
                    print("\n[SUCESSO] Item cadastrado no inventário!")
                else:
                    print("\n[FALHA] Não foi possível cadastrar o item.")
            
            except ValueError:
                print("\n[ERRO] Falha ao cadastrar: Peso ou Quantidade devem ser números válidos.")
            finally:
                print("-" * 20)

        elif opcao == '2':
            print("\n[Opção 2: Criar Pacote]")
            rastreio = input("Digite o Cód. de Rastreio: ")
            endereco = input("Digite o Endereço de entrega: ")
            
            sucesso = centro.criar_pacote(rastreio, endereco)
            if sucesso:
                print("\n[SUCESSO] Pacote criado!")
            else:
                print("\n[FALHA] Não foi possível criar o pacote.")
            print("-" * 20)

        elif opcao == '3':
            print("\n[Opção 3: Adicionar Item ao Pacote]")
            sku = input("Digite o SKU do item: ")
            rastreio = input("Digite o Cód. de Rastreio do pacote: ")
            
            sucesso = centro.adicionar_item_pacote(sku, rastreio)
            
            if sucesso: 
                print("\n[SUCESSO] Item adicionado ao pacote e estoque atualizado!") 
            else:
                print("\n[FALHA] Não foi possível adicionar o item.")
            print("-" * 20)

        elif opcao == '4':
            print("\n[Opção 4: Despachar Pacote]")
            rastreio = input("Digite o Cód. de Rastreio do pacote a despachar: ")
            
            # O método despachar_pacote já imprime a mensagem de sucesso/falha
            centro.despachar_pacote(rastreio)
            print("-" * 20)

        elif opcao == '5':
            # O método ver_invetario já imprime o relatório
            centro.ver_invetario()
            print("-" * 20)

        elif opcao == '6':
            # O método ver_pacotes já imprime o relatório
            centro.ver_pacotes()
            print("-" * 20)

        else:
            print("\n[ERRO] Opção inválida. Tente novamente.")
            print("-" * 20)

# Esta linha é necessária para executar a função main()
main()