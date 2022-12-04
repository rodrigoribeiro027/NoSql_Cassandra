import uuid 


def inserirVendedor(session):
    nome = input(str('Digite o nome do usuario: '))
    email = input(str('Digite o endereço de email: '))
    telefone = input(str('Digite o endereço de telefone: '))
    cpf = input(str('Digite o numero do cpf: '))
    endereco = input(str('Digite o endereço: '))
    session.execute("""
        insert into vendedor (id,nome,email,telefone,cpf,endereco) values ( %s,%s,%s,%s,%s,%s)
                """, (str(uuid.uuid1()), nome,email,telefone,cpf,endereco)
                )
    print('\nO Vendedro Foi Cadastrado :D\n')

def BuscaVendedor(session):
    print ("\n ----------------------------------- Listando Vendedores ----------------------------------- \n")
    for vendedor in session.execute('select * from vendedor'):
        print(f'id: {vendedor.id}')
        print(f'nome: {vendedor.nome}')
        print(f'email: {vendedor.email}')
        print(f'telefone: {vendedor.telefone}')
        print(f'cpf: {vendedor.cpf}')
        print(f'endereco: {vendedor.endereco}')
        print(f'-------------------------------------------------------------------------------------------')

def BuscaVendedorDetalhe(session):
    print ("\n ----------------------------------- Listando Vendedores ----------------------------------- \n")
    for vendedor in session.execute('select * from vendedor'):
        print(f'id: {vendedor.id}')
        print(f'nome: {vendedor.nome}')
        print(f'email: {vendedor.email}')
        print(f'-------------------------------------------------------------------------------------------')


def deleteVendedor(session):
    BuscaVendedorDetalhe(session)
    VendedorNome = input(str('Digite o id do vendedor que deseja excluir: '))
    session.execute(f"delete from vendedor where id='{VendedorNome}'")
    print(f'\nvendedor de id {VendedorNome} excluido com sucesso :D\n')

def atualizarVendedor(session):
    BuscaVendedorDetalhe(session)
    VendedorID = input(str('Digite o id do Usuario que deseja Atualizar: '))
    nome = input(str('Digite o nome do usuario: '))
    email = input(str('Digite o endereço de email: '))
    telefone = input(str('Digite o endereço de telefone: '))
    cpf = input(str('Digite o numero do cpf: '))
    endereco = input(str('Digite o endereço: '))
    session.execute(f"update vendedor set nome='{nome}',email='{email}',  telefone='{telefone}', cpf='{cpf}', endereco='{endereco}' where id='{VendedorID}'")
    print("\nVendedor Alterado :D\n")

