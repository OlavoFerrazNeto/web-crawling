import mysql.connector
from mysql.connector import Error

def conectar_mysql():
    try:
        # Configurações da conexão
        conexao = mysql.connector.connect(
            host="localhost",      
            user="root",         
            password="NauticoFerraz15!",  
            database="database_on_case"
        )

        if conexao.is_connected():
            print("✅ Conexão bem-sucedida ao MySQL!")
            return conexao

    except Error as e:
        print(f"❌ Erro ao conectar: {e}")
        return None

def fechar_conexao(conexao):
    if conexao and conexao.is_connected():
        conexao.close()
        print("🔒 Conexão encerrada.")

def criar_tabela():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",         
            password="NauticoFerraz15!", 
            database="database_on_case"
        )

        if conexao.is_connected():
            cursor = conexao.cursor()

            sql = """
            CREATE TABLE IF NOT EXISTS content_tech (
                id INT AUTO_INCREMENT PRIMARY KEY,
                quantidade_palavras INT,
                qtd_frases INT,
                quantidade_caracteres INT,
                media_palavras_frase FLOAT,
                proporcao_unicas FLOAT,
                proporcao_maiusculas FLOAT,
                palavras_curtas INT,
                palavras_longas INT,
                flesch FLOAT,
                flesch_kincaid FLOAT,
                smog FLOAT,
                coleman_liau FLOAT,
                sentimento FLOAT,
                subjetividade FLOAT,
                url TEXT,
                frases TEXT,
                create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """

            cursor.execute(sql)
            conexao.commit()
            print("✅ Tabela 'content_tech' criada/verificada com sucesso.")

    except Error as e:
        print(f"❌ Erro ao criar tabela: {e}")

    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
            print("🔒 Conexão encerrada.")


def inserir_content_tech(dados):
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",          
            password="NauticoFerraz15!", 
            database="database_on_case"
        )

        if conexao.is_connected():
            cursor = conexao.cursor()

            # Verificar se já existe registro com mesma URL e frases
            sql_check = """
                SELECT id FROM content_tech
                WHERE url = %s AND frases = %s
                LIMIT 1;
            """
            cursor.execute(sql_check, (dados["url"], dados["frases"]))
            existe = cursor.fetchone()

            if existe:
                print("⚠️ Registro já existe. Nenhuma inserção feita.")
                return False

            # Inserir novo registro
            sql_insert = """
                INSERT INTO content_tech (
                    quantidade_palavras, qtd_frases, quantidade_caracteres,
                    media_palavras_frase, proporcao_unicas, proporcao_maiusculas,
                    palavras_curtas, palavras_longas, flesch, flesch_kincaid,
                    smog, coleman_liau, sentimento, subjetividade, url, frases
                ) VALUES (
                    %(quantidade_palavras)s, %(qtd_frases)s, %(quantidade_caracteres)s,
                    %(media_palavras_frase)s, %(proporcao_unicas)s, %(proporcao_maiusculas)s,
                    %(palavras_curtas)s, %(palavras_longas)s, %(flesch)s, %(flesch_kincaid)s,
                    %(smog)s, %(coleman_liau)s, %(sentimento)s, %(subjetividade)s,
                    %(url)s, %(frases)s
                );
            """

            cursor.execute(sql_insert, dados)
            conexao.commit()
            print("✅ Registro inserido com sucesso!")
            return True

    except Error as e:
        print(f"❌ Erro ao inserir dados: {e}")
        return False

    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()


def ler_todos_content_tech():
    """
    Lê todos os registros da tabela content_tech.
    Retorna uma lista de dicionários.
    """
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",          
            password="NauticoFerraz15!", 
            database="database_on_case"
        )
        if conexao.is_connected():
            cursor = conexao.cursor(dictionary=True) 

            cursor.execute("SELECT * FROM content_tech;")
            registros = cursor.fetchall()

            print(f"✅ {len(registros)} registros encontrados.")
            return registros

    except Error as e:
        print(f"❌ Erro ao ler dados: {e}")
        return []

    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
            print("🔒 Conexão encerrada.")


# if __name__ == "__main__":
#     dados = ler_todos_content_tech()
#     for linha in dados:
#         print(linha)
# if __name__ == "__main__":
#     novo_dado = {
#         "quantidade_palavras": 100,
#         "qtd_frases": 5,
#         "quantidade_caracteres": 500,
#         "media_palavras_frase": 20.0,
#         "proporcao_unicas": 0.75,
#         "proporcao_maiusculas": 0.05,
#         "palavras_curtas": 30,
#         "palavras_longas": 15,
#         "flesch": 70.5,
#         "flesch_kincaid": 8.2,
#         "smog": 7.5,
#         "coleman_liau": 10.1,
#         "sentimento": 0.2,
#         "subjetividade": 0.5,
#         "url": "https://exemplo.com/artigo",
#         "frases": "Essa é uma frase de teste."
#     }

#     inserir_content_tech(novo_dado)
