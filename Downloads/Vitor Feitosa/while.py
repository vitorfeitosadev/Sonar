compras = []

while True:
    item = input("digite o proximo item ou  digite 'sair': ")
    if item.lower() == "sair":
        break
    compras.append(item)

print("\n Sua list de compras: ")
for item in compras:
    print(f" - {item}")