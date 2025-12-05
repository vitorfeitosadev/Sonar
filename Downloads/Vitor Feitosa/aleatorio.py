import random

numero = random.randint(1,50)
tentativas = 0  

print('Bem vindo ao jogo de advinhação')

while not acertou:
    chute = int(input('Digite um numero: '))
    tentativas += 1

    if tentativas == 10:
        print('Você PERDEU xD')
        break

    if numero > chute:
        print('O número Secreto é MENOR')
    elif numero < chute:
        print('O número Secreto é MAIOR')
    else:
        print(f'Parabens, você acertou')