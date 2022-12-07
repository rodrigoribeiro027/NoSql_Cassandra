import uuid

from Vendedor.vendedor import BuscaVendedorDetalhe

def inserir_produto(session):
        nome = input(str("Digite o nome do produto: "))
        preco = input(str("Digite o preço do produto: "))
        BuscaVendedorDetalhe(session)
        vendedor = input(str("Digite vendedor id do vendedor: "))
        session.execute("""
                insert into produto
                    (id, nome,  preco,vendedor)
                values
                    (%s,%s,%s,%s)
        """,
        (str(uuid.uuid1()),nome,  preco, vendedor))
        print(f'\nProduto de nome {nome} cadastrado com sucesso\n')
        print(f'-------------------------------------------------------------------------------------------')





def deletProduto(session):
    BuscaProdutoDetalhe(session)
    nome_produto = input(str('Digite o nome do produto que deseja excluir: '))
    session.execute(f"delete from produto where id='{nome_produto}'")
    print(f'\nProduto de nome {nome_produto} excluido com sucesso\n')


def BuscaProduto(session):
    print ("\n ----------------------------------- Listando Produtos -----------------------------------\n")
    for produto in session.execute('select * from produto'):
        print(f'nome: {produto.nome}')
        print(f'preco: {produto.preco}')
        print(f'vendedor: {produto.vendedor}')
        print(f'-------------------------------------------------------------------------------------------')




def BuscaProdutoDetalhe(session):
    print ("\n ----------------------------------- Listando Produtos -----------------------------------\n")
    for produto in session.execute('select * from produto'):
        print(f'id: {produto.id}')
        print(f'nome: {produto.nome}')
        print(f'preco: {produto.preco}')
        print(f'vendedor: {produto.vendedor}')
        print(f'-------------------------------------------------------------------------------------------')