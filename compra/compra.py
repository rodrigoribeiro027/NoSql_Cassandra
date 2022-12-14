import uuid
from produtos.produto import BuscaProdutoDetalhe
from usuario.usuario import BuscaUsuarioSelecao

def ComprarProduto(session):
    BuscaUsuarioSelecao(session)
    usuarioID = input(str('Digite o id do usuario: '))
    BuscaProdutoDetalhe(session)
    produtoID = input(str('Digite id do produto: '))
    Salvausuario = session.execute(f"select * from usuario where id ='{usuarioID}'")
    Salvaproduto = session.execute(f"select * from produto where id ='{produtoID}'")
    for usuario in Salvausuario:
        usuarioSelecionado = {'id':usuario.id, 'nome':usuario.nome, 'email':usuario.email ,'cpf':usuario.cpf,'endereco':usuario.endereco}
    for produto in Salvaproduto:
        produtoSelecionado = {'id':produto.id, 'nome':produto.nome, 'preco':produto.preco,'vendedor':produto.vendedor}
        PreçoProduto = produto.preco 
    session.execute("""
        insert into compra (id,usuario,produto,total) values (%s,%s,%s,%s)
                """, 
    (str(uuid.uuid1()),str(usuarioSelecionado),str(produtoSelecionado),str(PreçoProduto) ))
    print ("\n ----------------------------------- Compra Realizada :D ----------------------------------- \n")


def BuscaCompra(session):
    print ("\n ----------------------------------- Listando Compras ----------------------------------- \n")
    for compra in session.execute('select * from compra'):
        print(f'id: {compra.id}')
        print(f'Usuario: {compra.usuario}')
        print(f'Produto: {compra.produto}')
        print(f'Produto: {compra.total}')
        print(f'-------------------------------------------------------------------------------------------')

def BuscaCompraDetalhada(session):
    print ("\n ----------------------------------- Listando Compras ----------------------------------- \n")
    for compra in session.execute('select * from compra'):
        print(f'id: {compra.id}')
        print(f'Usuario: {compra.usuario}')
        print(f'Produto: {compra.produto}')
        print(f'-------------------------------------------------------------------------------------------')



def deleteCompra(session):
    BuscaCompra(session)
    CompraID = input(str('Digite o id da Compra que deseja excluir: '))
    session.execute(f"delete from compra where id='{CompraID}'")
    print(f'\nCompra de id {CompraID} excluido com sucesso\n')


def atualizarCompra(session):
    BuscaCompraDetalhada(session)
    CompraID = input(str('Digite o id do Compra: '))
    BuscaProdutoDetalhe(session)
    produtoID = input(str('Digite id do produto: '))
    SalvaCompra = session.execute(f"select * from compra where id ='{CompraID}'")
    Salvaproduto = session.execute(f"select * from produto where id ='{produtoID}'")
    for compra in SalvaCompra:
        for produto in Salvaproduto:
            produtoSelecionado = {'id':produto.id, 'nome':produto.nome, 'preco':produto.preco,'vendedor':produto.vendedor}
            PreçoProduto = produto.preco
            CompraSelecionado = {'id':compra.id, 'usuario':compra.usuario,'produto':produtoSelecionado, 'total':PreçoProduto}
    session.execute(f"delete from compra where id='{CompraID}'")
    session.execute("""
        insert into compra (id,usuario,produto,total) values (%s,%s,%s,%s)
                """, 
    (str(CompraSelecionado['id']),str(CompraSelecionado['usuario']),str(CompraSelecionado['produto']),str(CompraSelecionado['total']) ))
    print("\nCompra Alterado :D\n")
    print(f'-------------------------------------------------------------------------------------------')


