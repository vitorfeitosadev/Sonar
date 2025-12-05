def linha(text):
    print(text * 30)

linha("-")
print("Mensagem importante!")
linha(";")


def listar(qualquer):
    print(f" ->> {qualquer}")

lista = ["maça", "banana", "macaco", "linguiça"]

for argumento in lista:
    listar(argumento)