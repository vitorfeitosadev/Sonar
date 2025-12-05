senha_correta = "python123"
tentativa = input("Digite a senha: ")
num_tentativas = 0

while (tentativa != senha_correta) and (num_tentativas<5):
    print("Senha incorreta, tente novamente.")
    tentativa = input(f"Você tem {5 - num_tentativas} tentativas, digite a Senha:")
    num_tentativas += 1

if num_tentativas == 5:
    print("Acesso Bloqeuado, limite de tentativas excedido")
else:
    print("Acesso permitido")