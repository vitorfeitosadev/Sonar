notas = [8.5, 7.0, 9.2, 6.8]
soma = 0

for i in notas:
    soma += i

media = soma / len(notas)
print(f"Média: {media:.1f}")