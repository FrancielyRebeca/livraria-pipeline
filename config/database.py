import os
import psycopg2 
from dotenv import load_dotenv 

load_dotenv()

def conecta_db():

    try:
        conexao = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )

        print('Conexão com PostgreSQL bem sucessida.')
        return conexao

    except Exception as erro:
        print(f'Conexão com PostgreSQL mal sucedida. Causa: {erro}')
        return None 


def fecha_db(conexao, cursor=None):
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()
        print('Conexão com o banco livraria_db encerrada com sucesso.')


if __name__ == '__main__':
    minha_conexao = conecta_db()
    if minha_conexao:
        fecha_db(minha_conexao)