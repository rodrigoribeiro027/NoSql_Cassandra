import uuid 

def inserir_usuario(session):
    
    email = input(str('Digite o endereço de email: '))
    nome = input(str('Digite o nome do usuario: '))
    cpf = input(str('Digite o numero do cpf: '))
    endereco = input(str('Digite o endereço: '))
    session.execute("""
        insert into usuario (id,email,nome,cpf,endereco) values ( %s,%s,%s,%s,%s)
                """, (str(uuid.uuid1()), email,nome, cpf, endereco)
                )
    print('O Usuario Foi Cadastrado :D\n')


def deleteUsuario(session):
    BuscaUsuario(session)
    usuarioNome = input(str('Digite o id do usuario que deseja excluir: '))
    session.execute(f"delete from usuario where id='{usuarioNome}'")
    print(f'\nusuario de id {usuarioNome} excluido com sucesso...\n')


def BuscaUsuario(session):
    print ("\n ----------------------------------- Listando Usuarios ----------------------------------- \n")
    for usuario in session.execute('select * from usuario'):
        print(f'id: {usuario.id}')
        print(f'nome: {usuario.nome}')
        print(f'email: {usuario.email}')
        print(f'cpf: {usuario.cpf}')
        print(f'endereco: {usuario.endereco}')
        print(f'-------------------------------------------------------------------------------------------')

def atualizarUsuario(session):
    BuscaUsuario(session)
    usuarioid = input(str('Digite o id do Usuario que deseja Atualizar: '))
    nome = input(str('Digite o nome do usuario: '))
    email = input(str('Digite o endereço de email: '))
    cpf = input(str('Digite o numero do cpf: '))
    endereco = input(str('Digite o endereço: '))
    session.execute(f"update usuario set nome='{nome}', cpf='{cpf}', email='{email}', endereco='{endereco}' where id='{usuarioid}'")
    print("\nUsuario Alterado :D\n")