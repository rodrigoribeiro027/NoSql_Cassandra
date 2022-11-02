
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': 'secure-connect-cassandra.zip'
}
auth_provider = PlainTextAuthProvider('UodQtmnAfrIHplpeSxvUIfqU', 'nAEupo89GW-KbTMkMwFs7MQfFaRsJAEkvDuJfGyKBekG0zBinzp2.YLJ+FbRu5SkYKlZMmAmZQYDw40OCwHOqWQITqSkZJQBQTMX+gj-MqUFTTBgAydl7WTYMZ2izco9')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('mercado_livre')

row = session.execute("select release_version from system.local").one()

print("Criando Tabelas")
session.execute(
    "CREATE TABLE IF NOT EXISTS usuario (email text PRIMARY KEY, nome text, cpf text, endereco text, favorito text);")
print("Tabela Usuario Criada Com Sucesso\n")
session.execute(
    "CREATE TABLE IF NOT EXISTS vendedor (email text PRIMARY KEY, nome text, cpf text, endereco text);")
print("Tabela Vendedor Criada Com Sucesso\n")
session.execute(
    "CREATE TABLE IF NOT EXISTS produtos (id text PRIMARY KEY, nome text, preco text, vendedor text);")
print("Tabela Produtos Criada Com Sucesso\n")
session.execute(
    "CREATE TABLE IF NOT EXISTS compra (id text PRIMARY KEY, usuario text, produto text, total text);")
print("Tabelas Geradas Com Sucesso.")

execucao = True
while execucao:
    print('''Escolha Uma Opção:\n
- [0]Parar Aplicacão\n
- [1]Menu Vendedor\n
- [2]Menu Usuario\n
- [3]Menu Produtos\n

''')
    escolha = input(str('escolha Uma Obção:'))
    match escolha:
        case '0':
            break
        case '1':
            break
        case '2':
            break
        case '3':
            break

if row:
    print("ConexÃ£o bem sucedida...")
    print(row[0])
    
else:
    print("Ocorreu um erro.")