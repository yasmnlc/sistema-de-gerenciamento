# 🐱🐶 Sistema de Gerenciamento de Adoção de Animais 

Este projeto é um sistema de gerenciamento de adoção de animais, desenvolvido em Python, utilizando o framework **Streamlit** para a interface gráfica e **PostgreSQL** como banco de dados. O sistema permite realizar operações como inserir, consultar, atualizar e excluir dados sobre "Lar Temporário" e "Adotante".

## 💻 Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada.
- **Streamlit**: Framework para criação da interface do usuário.
- **PostgreSQL**: Banco de dados relacional para armazenamento das informações.
- **SQLAlchemy**: ORM utilizado para interagir com o banco de dados.
- **psycopg2**: Biblioteca para conectar o Python ao PostgreSQL e executar comandos SQL.

## 📋 Funcionalidades

- **Inserir dados**: Permite inserir novos registros nas tabelas `LarTemporario` e `Adotante`.
- **Consultar dados**: Permite pesquisar e visualizar dados das tabelas `LarTemporario` e `Adotante`.
- **Atualizar dados**: Permite atualizar registros existentes nas tabelas.
- **Excluir dados**: Permite excluir registros de ambas as tabelas.

## 📥 Instalação

Para rodar este projeto, siga os passos abaixo:

### 1. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 2. Execute o aplicativo Streamlit

```bash
streamlit run main.py
```