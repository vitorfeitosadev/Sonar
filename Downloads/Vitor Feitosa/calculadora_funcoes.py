def calculadora(x, y, operacao):
    if operacao == 1:
        (print(x + y))
    elif operacao == 2:
        (print(x - y))
    elif operacao == 3:
        (print(x * y))
    elif operacao == 4:
        (print(x / y))
    elif operacao == 5:
        (print(x % y))
    else: 
        print("Operacao invalida!")

while True:
    calculadora(float(input("digite um numero: ")),float(input("digite outro numero: ")),int(input("qual operação você quer fazer:\n1 para soma\n2 para subtracao \n3 para multiplicação\n4 para divisão\n5 para resto de divisão\n -> ")))
    repetir = (input("quer continuar calculando? (y/n)").lower())
    if repetir != "y":
        break