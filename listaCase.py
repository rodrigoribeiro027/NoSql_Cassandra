import usuario.usuario as inserirUsuario
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': 'secure-connect-cassandra.zip'
}
auth_provider = PlainTextAuthProvider('UodQtmnAfrIHplpeSxvUIfqU', 'nAEupo89GW-KbTMkMwFs7MQfFaRsJAEkvDuJfGyKBekG0zBinzp2.YLJ+FbRu5SkYKlZMmAmZQYDw40OCwHOqWQITqSkZJQBQTMX+gj-MqUFTTBgAydl7WTYMZ2izco9')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('mercado_livre')

def CaseUsuario(session):
    execucao = True
    while execucao:
        print('''Escolha Uma Opção:\n
        - [0]Voltar\n
        - [1]CadastrarUsuario\n
        - [2]DeletarUsuario\n
        - [3]BuscaUsuario\n
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