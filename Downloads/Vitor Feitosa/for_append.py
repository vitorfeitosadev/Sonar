nomes = []
for i in range(3):
    nome = input(f"Digite o {i+1} o nome! ")
    nomes.append(nome)

    """Código mais otimizado (menos uma variavel)
    nomes.append(input(f"Digite o {1+1} o nome))"""

print("\n Nomes cadastrados")
for nome in nomes:
    print(f"- {nome}")