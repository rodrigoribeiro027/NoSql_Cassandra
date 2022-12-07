import usuario.usuario as inserirUsuario
import produtos.produto as produto
import Vendedor.vendedor as vendedor
import compra.compra as compra

def CaseUsuario(session):
    execucao = True
    while execucao:
        print('''Escolha Uma Opção:\n
        - [0]Voltar\n
        - [1]Cadastrar\n
        - [2]Deletar\n
        - [3]Buscar\n
        - [4]Atualizar\n

        ''')
        escolha = input(str('escolha Uma Obção:'))
        match escolha:
            case '0':
                return
            case '1':
                inserirUsuario.inserir_usuario(session)
                break
            case '2':
                inserirUsuario.deleteUsuario(session)
                break
            case '3':
                inserirUsuario.BuscaUsuario(session)
                break
            case '4':
                inserirUsuario.atualizarUsuario(session)
                break

def CaseProduto(session):
    execucao = True
    while execucao:
        print('''Escolha Uma Opção:\n
        - [0]Voltar\n
        - [1]Cadastrar\n
        - [2]Deletar\n
        - [3]Buscar\n
        - [4]Atualizar\n

        ''')
        escolha = input(str('escolha Uma Obção:'))
        match escolha:
            case '0':
                return
            case '1':
                produto.inserir_produto(session)
                break
            case '2':
                produto.deletProduto(session)
                break
            case '3':
                produto.BuscaProduto(session)
                break
            case '4':
                inserirUsuario.atualizarUsuario(session)
                break

def CaseVendedor(session):
    execucao = True
    while execucao:
        print('''Escolha Uma Opção:\n
        - [0]Voltar\n
        - [1]Cadastrar\n
        - [2]Deletar\n
        - [3]Buscar\n
        - [4]Atualizar\n

        ''')
        escolha = input(str('escolha Uma Obção:'))
        match escolha:
            case '0':
                return
            case '1':
               vendedor.inserirVendedor(session)
            case '2':
               vendedor.deleteVendedor(session)
            case '3':
               vendedor.BuscaVendedor(session)
            case '4':
               vendedor.atualizarVendedor(session)

def CaseCompra(session):
    execucao = True
    while execucao:
        print('''Escolha Uma Opção:\n
        - [0]Voltar\n
        - [1]Compra\n
        - [2]Deletar\n
        - [3]Buscar\n
        - [4]Atualizar\n

        ''')
        escolha = input(str('escolha Uma Obção:'))
        match escolha:
            case '0':
                return
            case '1':
                compra.ComprarProduto(session)
            case '2':
                compra.deleteCompra(session)
            case '3':
                compra.BuscaCompra(session)
            case '4':
                compra.atualizarCompra(session)