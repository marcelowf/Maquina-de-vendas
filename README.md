# Vending-Machine

Este é um projeto simples de uma máquina de vendas em Python. A máquina de vendas suporta cinco produtos diferentes, cada um identificado por um código único. O usuário pode selecionar um produto inserindo o código correspondente, e a máquina verifica se o produto está em estoque. Se estiver disponível, a máquina solicitará dinheiro ao usuário até que o valor do produto seja alcançado. Em seguida, a máquina fornecerá o troco usando notas e moedas padrão.

## Funções

### `verificarProduto(produto)`

Esta função verifica se o código do produto inserido pelo usuário é válido. Caso contrário, solicita um código válido.

### `estoque(produto)`

Verifica se há estoque disponível para o produto escolhido. Retorna `True` se houver estoque, e `False` se estiver fora de estoque.

### `troco(valorProduto)`

Calcula e retorna o troco em notas e moedas, com base no valor do produto.

## Listas

- `notas`: Lista contendo os valores das notas e moedas disponíveis na máquina.
- `matriz`: Matriz que armazena informações sobre os produtos, como código, nome, quantidade em estoque e preço.

## Interface

O programa possui uma interface simples que exibe os produtos disponíveis, seus códigos e valores. O usuário é solicitado a inserir o código do produto desejado. Se o produto estiver em estoque, o programa solicitará dinheiro até atingir o valor do produto. Em seguida, exibe as notas e moedas a serem recebidas como troco.

O estoque é atualizado após cada compra, e o programa continua executando indefinidamente, permitindo a seleção contínua de produtos.

## Execução

Execute o script Python e siga as instruções na interface para interagir com a máquina de vendas.

```bash
python maquina_de_vendas.py

