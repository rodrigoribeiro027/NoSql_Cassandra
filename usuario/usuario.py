from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import uuid

cloud_config = {
        'secure_connect_bundle': 'secure-connect-cassandra.zip'
}
auth_provider = PlainTextAuthProvider('UodQtmnAfrIHplpeSxvUIfqU', 'nAEupo89GW-KbTMkMwFs7MQfFaRsJAEkvDuJfGyKBekG0zBinzp2.YLJ+FbRu5SkYKlZMmAmZQYDw40OCwHOqWQITqSkZJQBQTMX+gj-MqUFTTBgAydl7WTYMZ2izco9')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('mercado_livre')

row = session.execute("select release_version from system.local").one()

def inserir_usuario(session):
    email = input(str('Digite o endereço de email: '))
    nome = input(str('Digite o nome do usuario: '))
    cpf = input(str('Digite o numero do cpf: '))
    endereco = input(str('Digite o endereço: '))
    session.execute("""
        insert into usuario (email,nome,cpf,endereco) values (%s,%s,%s,%s)
                """, (email,nome, cpf, endereco)
                )
    print('O Usuario Foi Cadastrado Com Sucesso !!!')


def deleteUsuario(session):
    BuscaUsuario(session)
    usuarioNome = input(str('Digite o id do usuario que deseja excluir: '))
    
    session.execute(f"delete from usuario where id='{usuarioNome}'")
    print(f'\nusuario de id {usuarioNome} excluido com sucesso...\n')


def BuscaUsuario(session):
    print ("\n ----------------------------------- Listando Usuarios ----------------------------------- \n")

    for usuario in session.execute('select * from usuario'):
        print(f'nome: {usuario.nome}')
        print(f'email: {usuario.email}')
        print(f'cpf: {usuario.cpf}')
        print(f'endereco: {usuario.endereco}')
        print(f'----------------------------------------------------------------')