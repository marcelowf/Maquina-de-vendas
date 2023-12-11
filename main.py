# Importações
from time import sleep

# Definição da classe Produto
class Produto:
    def __init__(self, codigo, nome, estoque, preco):
        self.codigo = codigo
        self.nome = nome
        self.estoque = estoque
        self.preco = preco

# Função para verificar se o código do produto é válido
def verificarProduto(codigo):
    while codigo not in produtos_dict:
        print("Código de produto inválido!")
        codigo = int(input("Digite um código válido: "))
    return codigo

# Função para verificar se há estoque disponível
def temEstoque(codigo):
    return produtos_dict[codigo].estoque > 0

# Função para calcular e retornar o troco
def calcularTroco(valorProduto, dinheiro):
    troco = dinheiro - valorProduto
    troco_em_notas = []

    for nota in notas:
        while troco >= nota:
            troco -= nota
            troco_em_notas.append(nota)

    return troco_em_notas

# Inicialização dos produtos
produtos = [
    Produto(0, 'COCA-COLA', 2, 3.75),
    Produto(1, 'PEPSI', 5, 3.67),
    Produto(2, 'MONSTER', 1, 9.96),
    Produto(3, 'CAFÉ', 100, 1.25),
    Produto(4, 'REDBULL', 2, 13.99)
]

# Criação de um dicionário para facilitar o acesso aos produtos por código
produtos_dict = {produto.codigo: produto for produto in produtos}

# Lista de notas e moedas
notas = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]

# Interface
while True:
    print("Produtos Disponíveis:")
    for produto in produtos:
        print(f"Código: {produto.codigo} - {produto.nome} - R${produto.preco:.2f} - Estoque: {produto.estoque}")

    codigo_produto = int(input("Digite o código do produto desejado: "))
    codigo_produto = verificarProduto(codigo_produto)

    if temEstoque(codigo_produto):
        produto_selecionado = produtos_dict[codigo_produto]
        print(f"Produto selecionado: {produto_selecionado.nome} - R${produto_selecionado.preco:.2f}")
        
        dinheiro_inserido = float(input(f"Insira dinheiro até atingir R${produto_selecionado.preco:.2f}: "))

        if dinheiro_inserido < produto_selecionado.preco:
            print("Dinheiro insuficiente. Cancelando operação.")
        else:
            troco_em_notas = calcularTroco(produto_selecionado.preco, dinheiro_inserido)

            print("Troco em notas e moedas:")
            for nota in troco_em_notas:
                print(f"R${nota:.2f}")

            produto_selecionado.estoque -= 1
            print("Compra realizada com sucesso!")

    else:
        print("Esté produto está fora de estoque no momento")

    print("=-" * 21)
    sleep(4)
