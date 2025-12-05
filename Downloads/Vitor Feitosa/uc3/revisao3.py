# � Revisão de POO: Sistema de Pedidos "JWC Pizza"
# Contexto do Desafio: Parabéns, você foi aprovado na primeira etapa do processo seletivo
# da JWC! Seu primeiro projeto como desenvolvedor júnior na empresa é criar um sistema
# interno em Python para gerenciar pedidos para o novo cliente da JWC, a "JWC Pizza".
# Tempo Estimado: 2 horas Dificuldade: Iniciante / Intermediário
# Objetivos de Aprendizagem:
# ● Criar múltiplas classes (Pizza, Pedido).
# ● Usar o construtor __init__ com múltiplos atributos.
# ● Implementar métodos de instância (funções dentro de uma classe).
# ● Praticar composição (um objeto Pedido "contém" objetos Pizza).
# ● Usar lógica de programação (loops e condicionais) dentro dos métodos.
# ● Praticar encapsulamento (uso de atributos "privados" como __total).

class Pizza:
    # Atributos de CLASSE (constantes)
    PRECOS_SABOR = {
        "calabresa": 5.00,
        "mussarela": 5.00,
        "frango": 10.00,
        "portuguesa": 10.00,
        "camarao": 20.00,
        "banana nevada": 30.00
    }
    
    PRECOS_TAMANHO = {
        "pequena": 30.00,
        "media": 45.00,
        "grande": 60.00
    }

    def __init__(self, sabor: str, tamanho: str, ingredientes: list):
        # Atributos de INSTÂNCIA
        self.sabor = sabor.lower().strip()
        self.tamanho = tamanho.lower().strip()
        self.ingredientes = ingredientes # Mantendo sua lista de ingredientes

    def calcular_valor_total(self) -> float:
        """Calcula o valor da pizza somando o preço base do sabor e o preço fixo do tamanho."""
        
        # Busca o valor no dicionário de sabor usando self.sabor como chave
        preco_sabor = self.PRECOS_SABOR.get(self.sabor, 0.0)
        
        # Busca o valor no dicionário de tamanho usando self.tamanho como chave
        preco_tamanho = self.PRECOS_TAMANHO.get(self.tamanho, 0.0)
        
        valor_total = preco_sabor + preco_tamanho
        return valor_total
        
class Pedido:
    def __init__(self, cliente: str, endereco: str):
        self.cliente = cliente
        self.endereco = endereco
        
        # O atributo que armazena as pizzas DEVE SER UMA LISTA
        self.pizzas_no_pedido: list[Pizza] = [] 
        
        # O total será recalculado a cada adição/remoção de pizza
        self.__total = 0.0 

    def adicionar_pizza(self, pizza: Pizza):
        """Adiciona um objeto Pizza à lista de pizzas do pedido."""
        # O .append() é o método correto para adicionar um item a uma lista
        self.pizzas_no_pedido.append(pizza)
        print(f"Pizza de {pizza.sabor} adicionada ao pedido do cliente {self.cliente}.")
        
        # Opcional: Recalcular o total imediatamente após adicionar
        self.recalcular_total()

    def recalcular_total(self):
        """Recalcula o valor total somando o preço de CADA pizza na lista."""
        total_acumulado = 0.0
        
        # Itera sobre CADA objeto Pizza dentro da lista self.pizzas_no_pedido
        for pizza_item in self.pizzas_no_pedido:
            # Chama o método de cálculo de valor da própria Pizza
            total_acumulado += pizza_item.calcular_valor_total()
            
        self.__total = total_acumulado # Armazena no atributo encapsulado

    def obter_total(self) -> float:
        """Getter para acessar o valor total encapsulado."""
        return self.__total

    def __str__(self):
        """Para uma impressão amigável do pedido."""
        detalhes = f"--- PEDIDO --- \nCliente: {self.cliente} | Endereço: {self.endereco}\n"
        detalhes += f"Total de Pizzas: {len(self.pizzas_no_pedido)}\n"
        detalhes += f"VALOR TOTAL: R$ {self.__total:.2f}"
        return detalhes


print("Seja bem vindo(a) a JWC Pizzaria!")
cliente = (input('Para começarmos digite seu nome: '))
endereco = (input('Agora escreva seu endereco: '))
sabor = (input('Digite o numero correspondente ao sabor que deseja\n1.Calabresa \n2.Mussarela \n3.Frango \n4.Portuguesa \n5.Camarão \n6.Banana Nevada: '))
tamanho = (input('Escolha o tamanho que deseja\n1.pequeno (30cm) \n2.medio (45cm) \n3.grande (60cm)'))
if sabor == "1":
    

        