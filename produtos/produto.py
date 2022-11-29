import uuid


from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
cloud_config = {
        'secure_connect_bundle': 'secure-connect-cassandra.zip'
}
auth_provider = PlainTextAuthProvider('UodQtmnAfrIHplpeSxvUIfqU', 'nAEupo89GW-KbTMkMwFs7MQfFaRsJAEkvDuJfGyKBekG0zBinzp2.YLJ+FbRu5SkYKlZMmAmZQYDw40OCwHOqWQITqSkZJQBQTMX+gj-MqUFTTBgAydl7WTYMZ2izco9')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('mercado_livre')


def inserir_produto(session):
    execucao = True
    while execucao:

        nome = input(str("Digite o nome do produto: "))
        descricao = input(str("Digite a descrição do produto: "))
        preco = input(str("Digite o preço do produto: "))
        vendedor = input(str("Digite vendedor: "))

        session.execute("""
                insert into produto
                    (id, nome, descricao, preco,vendedor)
                values
                    (%s,%s,%s,%s,%s)
        """,
        (str(uuid.uuid1()),nome, descricao, preco, vendedor))
        break


def deletProduto(session):
    BuscaProduto(session)
    nome_produto = input(str('Digite o nome do produto que deseja excluir: '))
    session.execute(f"delete from produto where id='{nome_produto}'")
    print(f'\nProduto de nome {nome_produto} excluido com sucesso\n')


def BuscaProduto(session):
    print ("\n ----------------------------------- Listando Produtos -----------------------------------\n")
    for produto in session.execute('select * from produto'):
        print(f'nome: {produto.nome}')
        print(f'descricao: {produto.descricao}')
        print(f'preco: {produto.preco}')
        print(f'vendedor: {produto.vendedor}')
        print(f'-------------------------------------------------------------------------------------------')