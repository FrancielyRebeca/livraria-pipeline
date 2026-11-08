import sys
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.database import conecta_db, fecha_db

def popular_clientes(cursor):
    sql_clientes = 'INSERT INTO clientes(nome, email, cidade) VALUES(%s, %s, %s);'

    dados_clientes = [
        ("Ana Silva", "ana.silva@email.com", "São Paulo"), 
        ("Carlos Souza", "carlos.souza@email.com", "Rio de Janeiro"), 
        ("Mariana Costa", "mariana.costa@email.com", "Belo Horizonte"),
        ("João Pereira", "joao.pereira@email.com", "Curitiba") 
    ]

    cursor.executemany(sql_clientes, dados_clientes)
    print('Inserção de clientes bem sucedida!')


def popular_livros(cursor):
    sql_livros = 'INSERT INTO livros(titulo, categoria, preco) VALUES(%s, %s, %s);'

    dados_livros = [
        ("Python para Análise de Dados", "Tecnologia", 89.90), 
        ("PostgreSQL Prático", "Tecnologia", 75.00),
        ("Domine o Power BI", "Tecnologia", 95.50), 
        ("Gestão de Negócios", "Negócios", 60.00), 
        ("O Poder do Hábito", "Desenvolvimento Pessoal", 45.00)
    ]

    cursor.executemany(sql_livros, dados_livros)
    print('Inserção de livros bem sucedida!')


def popular_vendas(cursor):
    sql_vendas = 'INSERT INTO vendas(id_cliente, id_livro, data_venda, quantidade, valor_total) VALUES(%s, %s, %s, %s, %s);'

    dados_vendas = [
        (1, 1, '2026-10-01', 2, 179.80),
        (2, 3, '2026-10-02', 1, 95.50), 
        (3, 2, '2026-10-05', 1, 75.00), 
        (4, 5, '2026-10-10', 3, 135.00), 
        (1, 4, '2026-10-15', 1, 60.00), 
        (2, 1, '2026-10-20', 1, 89.90), 
        (3, 3, '2026-11-01', 2, 191.00)
    ]

    cursor.executemany(sql_vendas, dados_vendas)
    print('Inserção de vendas bem sucedida!')

def popular_livraria():
    conexao = conecta_db()
    if not conexao:
        return 

    cursor = conexao.cursor()
    try:
        print('Iniciando...')

        popular_clientes(cursor)
        popular_livros(cursor)
        popular_vendas(cursor)

        conexao.commit()
        print('Dados salvos.')
    except Exception as erro:
        conexao.rollback()
        print(f'Operações canceladas. Motivo: {erro}')

    finally:
        fecha_db(conexao, cursor)


if __name__ == '__main__':
    popular_livraria()
    