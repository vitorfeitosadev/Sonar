def saque_notas(valor_saque):
    return [(valor_saque/5), (valor_saque/10), (valor_saque/20), (valor_saque/50), (valor_saque/100)]

saque_notas(int(input("Digite o valor que deseja sacar")))
