
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import listaCase  as listadecases


def conexao():
    cloud_config= {
            'secure_connect_bundle': 'secure-connect-cassandra.zip'
    }
    auth_provider = PlainTextAuthProvider('UodQtmnAfrIHplpeSxvUIfqU', 'nAEupo89GW-KbTMkMwFs7MQfFaRsJAEkvDuJfGyKBekG0zBinzp2.YLJ+FbRu5SkYKlZMmAmZQYDw40OCwHOqWQITqSkZJQBQTMX+gj-MqUFTTBgAydl7WTYMZ2izco9')
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect('mercado_livre')
    return session

cloud_config= {
            'secure_connect_bundle': 'secure-connect-cassandra.zip'
    }
auth_provider = PlainTextAuthProvider('UodQtmnAfrIHplpeSxvUIfqU', 'nAEupo89GW-KbTMkMwFs7MQfFaRsJAEkvDuJfGyKBekG0zBinzp2.YLJ+FbRu5SkYKlZMmAmZQYDw40OCwHOqWQITqSkZJQBQTMX+gj-MqUFTTBgAydl7WTYMZ2izco9')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('mercado_livre')

# Tabelas do banco Cassandra abaixo:

print("Criando Tabelas")

session.execute(
    "CREATE TABLE IF NOT EXISTS usuario (id text PRIMARY KEY,email text , nome text, cpf text, endereco text);")
print("Tabela Usuario Criada Com Sucesso\n")

session.execute(
    "CREATE TABLE IF NOT EXISTS produto (id text PRIMARY KEY, nome text, preco text, vendedor text);")
print("Tabela Produtos Criada Com Sucesso\n")

session.execute(
    "CREATE TABLE IF NOT EXISTS compra (id text PRIMARY KEY, usuario text, produto text, total text);")
print("Tabela Compras Criada Com Sucesso\n")

session.execute(
    "CREATE TABLE IF NOT EXISTS vendedor (id text PRIMARY KEY,nome text,email text, cpf text, endereco text, telefone text );")
print("Tabela Usuario Criada Com Sucesso\n")

print("Tabelas Geradas Com Sucesso.")

execucao = True
while execucao:
    print('''Escolha Uma Opção:\n
- [0]Parar Aplicacão\n
- [1]Menu Usuario\n
- [2]Menu Produto\n
- [3]Menu Compra\n
- [4]Menu Vendedor\n
''')

    escolha = input(str('escolha Uma Obção:'))
    match escolha:
        case '0':
            print('Até mais...')
            execucao = False
        case '1':
            listadecases.CaseUsuario(session)
        case '2':
            listadecases.CaseProduto(session)
        case '3':
            listadecases.CaseCompra(session)
        case '4':
            listadecases.CaseVendedor(session)
