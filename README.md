# Maquina-de-vendas
#verificarProduto
def verificarProduto(produto):
    while int(produto) > 4 or int(produto) < 0:
        print("este código não existe")
        produto = input("coloque um código valido: ")
    return produto
#estoque
def estoque(produto):
    if matriz[int(produto)][2] <= 0:
        return False
    else:
        return True
#troco
def troco(valorProduto):
    listaDeNotas = []
    dinheiro = 0
    contador = 0
    while dinheiro < valorProduto:
        dinheiro += float(input("insira valores na maquina até atingir o valor {} : ".format(valorProduto)))
    retorno = dinheiro - valorProduto
    while contador < 13:
        if notas[contador] <= retorno:
            retorno -= notas[contador]
            listaDeNotas.append(notas[contador])
        else:
            contador += 1
    if retorno > 0.005:
        listaDeNotas.append(notas[12])
    return listaDeNotas
#listas
notas =[200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
matriz =[[0, 'COCA-COLA', 2, 3.75], [1, 'PEPSI', 5, 3.67], [2, 'MONSTER', 1, 9.96], [3, 'CAFÉ', 100, 1.25], [4, 'REDBULL', 2, 13.99]]
#interface
while True:
    for contador in range(5):
        print("""produto:{}   código:{}   valor:{}""".format((matriz[contador][1]), (matriz[contador][0]), (matriz[contador][3])))
    print("=-"*21)
    contadorX = 0
    produtoX = int(0)
    while contadorX == 0:
        produto = int(input("coloque o código do produto que deseja: "))
        produtoX = verificarProduto(produto)
        if estoque(produtoX) == True:
            contadorX += 1
        else:
            print("Esté produto está fora de estoque no momento")
    valorProduto = (matriz[produtoX][3])
    print("""notas e moedas a receber: 
""",troco(valorProduto))
    matriz[produtoX][2] -= 1
    from time import sleep
    print("=-"* 21)
    sleep(4)
