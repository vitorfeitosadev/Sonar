soma = 0
numero = int(input("Digite um número (Digite 0 para sair)"))

while numero != 0:
    soma += numero
    numero = int(input("Digite um número (Digite 0 para sair)"))

print(f"Aqui estã sua soma {soma}")