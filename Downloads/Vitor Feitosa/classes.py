class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome    #atributo
        self.idade = idade  #atributo
    
    def falar(self):            #Metodo
        print(f"{self.nome} está falando!")
    
    def aniversario(self):      #Metodo
        self.idade += 1
        print(f"{self.nome} fez aniversário! Agora tem {self.idade} anos!")
        
#Criando objetos (instâncias)

pessoa1 = Pessoa("Ana", 25)
pessoa2 = Pessoa("Carlos", 30)

pessoa1.falar()