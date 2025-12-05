def controle_de_senha(senha):
    tem8 = len(senha) >= 8
    temMaiuscula  = any(c.isupper() for c in senha)
    temNumero = any(c.isdigit() for c in senha)
    #temNumero = any(c.isnumeric() for c in senha)

    if not tem8: 
        print('Sua senha não atende ao número minimo de characters')
    if not temMaiuscula:
        print('Sua senha não contém um caracter maiusculo')
    if not temNumero:
        print('Sua senha não possuí um número')
    if tem8 and temMaiuscula and temNumero:
            print('Parabéns, você criou sua senha.')


senha = controle_de_senha(input('Crie uma senha: '))
#Desnecessário o print, já existe essa função dentro das condições
print(senha)