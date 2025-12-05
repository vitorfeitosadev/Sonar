class Usuarios:
    def __init__(self,nome,email):
        self.nome = nome
        self.email = email
        
    def exibir_info(self):
        print(f" O nome do usuário é {self.nome} e seu email é {self.email}! ")
        
class Admin(Usuarios):
    def acessar_config(self):
        print(f'{self.nome} acessou as configurações')
        
class Cliente(Usuarios):
    def comprar(self, produto):
        print(f'{self.nome} comprou {produto.nome} por {produto.valor}')
        
class Funcionario(Usuarios):
    def bater_ponto(self):
        print(f'{self.nome} bateu ponto')
        
Funcionario("Gostosinha", "gostosa@email.com").exibir_info()

class Produto:
    def __init__(self, nome, estoque, valor):
        self.nome = nome
        self.estoque = estoque
        self.valor = valor
        
lista_de_produtos = [Produto("Kingdom Hearts", 20, "R$ 500,00"), Produto("New World", 10, "R$ 100,00")]

Cliente('Joao', 'joao@email.com').comprar(lista_de_produtos[0])
        
        