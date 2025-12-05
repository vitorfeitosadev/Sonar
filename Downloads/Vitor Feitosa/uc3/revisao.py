class Cliente():
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Conta():
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.__saldo = 0.0

    #getter
    def consultar_saldo(self):
        return self.__saldo
    
    #setter
    def sacar(self, valor):
        """
        Subtrai um valor do saldo, se o valor for positivo
        e houver saldo suficiente.
        Retorna True em sucesso, False em falha.
        """
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            #self.__saldo = self.__saldo - valor
            return True
        return False
    
    def depositar(self, valor):
        """
        Adiciona um valor ao saldo, se o valor for positivo.
        Retorna True em sucesso, False em falha.
        """
        if valor > 0:
            self.__saldo += valor
            #self.__saldo = self.__saldo + valor
            return True
        return False


print("bem vindo ao PythonBank!\nCadastre-se agora :)")
usuario_atual = Cliente(input("Digite o seu nome:\n"), input("Digite o seu cpf:\n"))
conta_atual= Conta("12345", usuario_atual)

while True:
    print(f'Bem vindo {usuario_atual.nome}')
    opcao = input("Digite:\n1. Consultar Saldo\n2. Depositar\n3. Sacar\n4. Sair do Banco\n")
    if opcao == "1":
        print(f'\n R$ {conta_atual.consultar_saldo()}\n')
    elif opcao == "2":
        conta_atual.depositar(float(input("digite o valor que deseja depositar:\n")))
        print("Depósito feito com sucesso")
    elif opcao == "3":
        conta_atual.sacar(float(input("digite o valor que deseja sacar:\n")))
        print("Saque feito com sucesso")
    elif opcao == "4":
        break
    else:
        print("Opção inválida, tente novamente")

