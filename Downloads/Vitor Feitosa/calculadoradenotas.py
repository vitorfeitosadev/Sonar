nota1 =float(input("digite aqui sua primeira nota vida: "))
nota2 = float(input("digite aqui sua segunda nota coração: "))
nota3 = float(input("digite aqui sua terceira nota amor: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"parabéns, você foi aprovado com média: {media}")
elif 4 <= media <= 7:
    print(f"Você está de recuperação com média {media}, vamo que vamo!!")
else:
    print("Que pena gay, você foi reprovado")