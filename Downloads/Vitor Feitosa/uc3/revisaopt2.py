class Cliente():
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Conta():
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.__saldo = 0.0
        self.__extrato = []

    #getter
    def consultar_saldo(self):
        return self.__saldo
    
    def consultar_extrato(self):
        return self.__extrato
    
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
            self.__extrato.append(f'- R$ {valor}')
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
            self.__extrato.append(f'+ R$ {valor}')
            return True
        return False

    def transferir(self, valor, conta_destino):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            #self.__saldo = self.__saldo - valor
            self.__extrato.append(f'- R$ {valor}')
            conta_destino.depositar(valor)
            return True
        return False

conta_teste = Conta("12345", Cliente("teste", "87654321"))
contas = [conta_teste]


while True:
    print("bem vindo ao PythonBank!\n")
    opcao=input("Selecione a opção desejada:\n1. Login\n2. Cadastre uma nova conta\n3. Sair do sistema\n\n")
    conta_atual = None
    if opcao == "1":
        tentativa_login=input("Digite o seu CPF:\n")
        for i in contas:
            if i.cliente.cpf == tentativa_login:
                conta_atual=i
        if conta_atual == None:
            print("Conta não encontrada, tente novamente")
    elif opcao == "2":
        print("Preencha suas informações:")
        conta_atual = Conta("12345",Cliente(input("Digite seu nome:\n"), input("Digite seu CPF:\n")))
        contas.append(conta_atual)
    elif opcao == "3":
        break
    else:
        print("Opção inválida, tente novamente")
    while conta_atual!=None:
        print(f'Bem vindo {conta_atual.cliente.nome}')
        opcao = input("Selecione a opção desejada:\n1. Consultar Saldo\n2. Consultar Extrato\n3. Depositar\n4. Sacar\n5. Transferir\n6. Deslogar\n\n")
        if opcao == "1":
            print(f'\n R$ {conta_atual.consultar_saldo()}\n')
        elif opcao == "2":
            for i in conta_atual.consultar_extrato():
                print(i)
        elif opcao == "3":
            conta_atual.depositar(float(input("digite o valor que deseja depositar:\n")))
            print("Depósito feito com sucesso")
        elif opcao == "4":
            conta_atual.sacar(float(input("digite o valor que deseja sacar:\n")))
            print("Saque feito com sucesso")
        elif opcao == "5":
            localizar_conta=input("Digite a chave pix (CPF) para a conta que deseja transferir:\n")
            for i in contas:
                if i.cliente.cpf == localizar_conta:
                    conta_destino=i
            conta_atual.transferir(float(input("digite o valor que deseja transferir:\n")),conta_destino)
            #print(f'Saldo do destinatario: {conta_teste.consultar_saldo()}')
        elif opcao == "6":
            conta_atual=None
            break
        else:
            print("Opção inválida, tente novamente")

    