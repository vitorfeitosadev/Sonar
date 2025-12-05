# Função para converter Celsius -> Fahrenheit
def celsius_para_fahrenheit(temp_c):
    return (temp_c * 9/5) + 32
# Função para calcular a média das temperaturas
def media(temperaturas):
    return sum(temperaturas) / len(temperaturas)
# Função para listar dias acima da média
def dias_acima_media(temperaturas):
    m = media(temperaturas)
    dias = []
    for i in range(len(temperaturas)):   # percorre pelos índices
        if temperaturas[i] > m:
            dias.append((i + 1, temperaturas[i]))  # i+1 para começar do dia 1
    return dias

def dias_da_semana(dia):
    if dia == 1:
        return "domingo"
    if dia == 2:
        return "segunda-feira"
    if dia == 3:
        return "terça-feira"
    if dia == 4:
        return "quarta-feira"
    if dia == 5:
        return "quinta-feira"
    if dia == 6:
        return "sexta-feira"
    if dia == 7:
        return "sabado"        
    


# Programa principal
temperaturas_c = [22, 25, 21, 20, 27, 30, 26]  # exemplo
# Conversão para Fahrenheit
#for t in temperaturas_c:
#    temperaturas_f.append(celsius_para_fahrenheit(t))
temperaturas_f = [celsius_para_fahrenheit(t) for t in temperaturas_c]
print("Temperaturas em Celsius:", temperaturas_c)
print("Temperaturas em Fahrenheit:", temperaturas_f)
# Média
media_c = media(temperaturas_c)
print(f"\nTemperatura média da semana: {media_c:.0f}°C")

# Dias acima da média
print("\nDias com temperatura acima da média:")
for dia, temp in dias_acima_media(temperaturas_c):
    io = dias_da_semana(dia)
    print(f"{io}: {temp}°C")
