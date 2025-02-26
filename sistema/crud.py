from .connection import get_psycopg2_connection

def consultar_tabela(nome_tabela):
    conn = get_psycopg2_connection()
    if conn:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {nome_tabela}")
        colunas = [desc[0] for desc in cur.description]
        dados = cur.fetchall()
        cur.close()
        conn.close()

        return [dict(zip(colunas, row)) for row in dados]
    return []


def inserir_tabela(nome_tabela, colunas, valores):
    try:
        conn = get_psycopg2_connection()
        if conn:
            cur = conn.cursor()
            colunas_str = ", ".join(colunas)
            valores_placeholder = ", ".join(["%s"] * len(valores))
            query = f"INSERT INTO {nome_tabela} ({colunas_str}) VALUES ({valores_placeholder})"
            cur.execute(query, valores)
            conn.commit()
            cur.close()
            conn.close()
            return True, None
    except Exception as e:
        print(f"Erro ao inserir em {nome_tabela}: {e}")
        return False, str(e)


def atualizar_tabela(nome_tabela, id, novos_dados):
    try:
        if not novos_dados:
            print("Nenhum campo para atualizar.")
            return False

        conn = get_psycopg2_connection()
        if conn:
            cur = conn.cursor()
            campos = ", ".join([f"{chave} = %s" for chave in novos_dados.keys()])
            valores = list(novos_dados.values()) + [id]
            query = f"UPDATE {nome_tabela} SET {campos} WHERE id = %s"
            cur.execute(query, valores)
            conn.commit()
            cur.close()
            conn.close()
            return True
    except Exception as e:
        print(f"Erro ao atualizar {nome_tabela}: {e}")
        return False


def excluir_tabela(nome_tabela, id):
    try:
        conn = get_psycopg2_connection()
        if conn:
            cur = conn.cursor()
            cur.execute(f"SELECT id FROM {nome_tabela} WHERE id = %s", (id,))
            if cur.fetchone() is None:
                print(f"Erro: ID {id} não encontrado na tabela {nome_tabela}.")
                cur.close()
                conn.close()
                return False
            
            cur.execute(f"DELETE FROM {nome_tabela} WHERE id = %s", (id,))
            conn.commit()
            cur.close()
            conn.close()
            return True
    except Exception as e:
        print(f"Erro ao excluir de {nome_tabela}: {e}")
        return False
