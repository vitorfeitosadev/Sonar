#1 método mais simples com o laço for em listas
#produtos = ["mario", "Hollow Knight", "Xenoblade"]
#preços = [400, 60, 300]
#for i in range(len(produtos)): uma forma de fazer seria criar uma range para manter as 2 listas na mesma posição.

#2 método com "dicionario"
#produtos = [{"nome": "Mario", "preço": 400}, {"nome": "Hollow Knight", "preço": 60}, {"nome": "Xenoblade", "preço": 300}] 
#print(produtos[0][nome])  #especifique o atributo que você deseja puxar.
 
#3 - Método matriz
produtos = [["mario", 400], ['Hollow Knight', 60], ["Xenoblade", 300], ['Bayonetta', 200], ['KingdomHearts', 250]]
print(produtos[0][0]) #na matriz temos os dados jogados, ou seja, eles não possuem atributos como no dicionario, e a forma de acesso é somente pelas posições ou seja [] e o número desejado

def calc_produtos():
    total = 0
    for i in range(len(produtos)):
        total += produtos[i][1]
        return total
    
def caro_barato(vendasDia):
    produto_caro = vendasDia[0]
    produto_barato = vendasDia[0]
    for i in range(len(vendasDia)):

        if vendasDia[i][1] > produto_caro[1]:
            produto_caro = vendasDia[1]
        
        if vendasDia[i][1] < produto_barato[1]:
            produto_barato = vendasDia[1]

    return produto_barato, produto_caro

def produto_acima_100(produto):
    maisque100 = []
    for i in range(len(produto)):
        if produto[i][1]>100:
            maisque100.append(produto)
    return maisque100

maisCaro = caro_barato(produtos)[1]
maisBarato = caro_barato(produtos)[0]

print(f'O produto mais caro é {maisCaro} e o mais barato é {maisBarato}')








