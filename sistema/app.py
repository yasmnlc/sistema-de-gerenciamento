import streamlit as st
from .crud import *

def configurar_pagina():
    st.set_page_config(page_title="Sistema de Adoção", page_icon="🐱", layout="centered")
    col1, col2, col3 = st.columns([2, 2, 2])
    with col2:
        st.image('img/logo.png', width=200)

    st.markdown("<h1 style='text-align: center;'>Sistema de Gerenciamento de Adoção de Animais</h1>", unsafe_allow_html=True)


def selecionar_tabela_acao():
    tabela = st.selectbox("Escolha uma tabela", ["", "LarTemporario", "Adotante"])
    acao = st.selectbox("Escolha uma ação", ["", "Consultar", "Inserir", "Atualizar", "Excluir"])
    return tabela, acao


def inserir_dados(tabela_selecionada):
    if tabela_selecionada == "LarTemporario":
        st.subheader("Inserir Novo Lar Temporário")
        campos = {
            "NomeResponsavel": st.text_input("Nome do Responsável"),
            "CapacidadeMaxima": st.number_input("Capacidade Máxima", min_value=1),
            "Cidade": st.text_input("Cidade"),
            "Bairro": st.text_input("Bairro"),
            "Rua": st.text_input("Rua"),
            "NumeroCasa": st.text_input("Número")
        }
    elif tabela_selecionada == "Adotante":
        st.subheader("Inserir Novo Adotante")
        campos = {
            "Nome": st.text_input("Nome"),
            "CPF": st.text_input("CPF"),
            "Contato": st.text_input("Contato"),
            "Cidade": st.text_input("Cidade"),
            "Bairro": st.text_input("Bairro"),
            "Rua": st.text_input("Rua"),
            "NumeroEndereco": st.text_input("Número do Endereço")
        }
    
    if st.button("Inserir"):
        if all(campos.values()):
            sucesso, mensagem = inserir_tabela(tabela_selecionada, list(campos.keys()), list(campos.values()))
            if sucesso:
                st.success(f"{tabela_selecionada} inserido com sucesso!")
            else:
                st.error(f"Erro ao inserir em {tabela_selecionada}: {mensagem}.")
        else:
            st.error("Todos os campos são obrigatórios.")


def consultar_dados(tabela_selecionada):
    termo_pesquisa = st.text_input("Pesquise por qualquer informação do banco:")

    if st.button(f"Consultar {tabela_selecionada}"):
        dados = consultar_tabela(tabela_selecionada)
        
        if termo_pesquisa:
            resultados_filtrados = [
                item for item in dados
                if any(termo_pesquisa.lower() in str(valor).lower() for valor in item.values())
            ]
            if resultados_filtrados:
                st.write(f"Resultados encontrados na tabela {tabela_selecionada}:")
                st.write(resultados_filtrados)
            else:
                st.warning(f"Nenhum resultado encontrado para '{termo_pesquisa}'. Exibindo todos os dados.")
                st.write(dados)
        else:
            st.write(f"Exibindo todos os dados da tabela {tabela_selecionada}:")
            st.write(dados)


def atualizar_dados(tabela_selecionada):
    st.subheader(f"Atualizar {tabela_selecionada}")
    id_atualizar = st.number_input("ID a atualizar", min_value=1)
    dados = consultar_tabela(tabela_selecionada)
    item_atual = next((item for item in dados if item['id'] == id_atualizar), None)
    
    if item_atual:
        st.write("Dados atuais:", item_atual)
        novos_dados = {}
        for campo in item_atual.keys():
            if campo != "id":
                valor = st.text_input(f"Novo {campo}", value=str(item_atual[campo]))
                if valor:
                    novos_dados[campo] = valor
        if st.button("Atualizar"):
            if atualizar_tabela(tabela_selecionada, id_atualizar, novos_dados):
                st.success(f"{tabela_selecionada} atualizado com sucesso!")
            else:
                st.error(f"Erro ao atualizar {tabela_selecionada}.")
    else:
        st.warning("ID não encontrado.")


def excluir_dados(tabela_selecionada):
    st.subheader(f"Excluir {tabela_selecionada}")
    id_excluir = st.number_input("ID a excluir", min_value=1, step=1)
    dados = consultar_tabela(tabela_selecionada)
    item_atual = next((item for item in dados if item['id'] == id_excluir), None)

    if item_atual:
        st.write(f"Dados do {tabela_selecionada} a excluir:", item_atual)  
        if st.button("Confirmar Exclusão"):
            if excluir_tabela(tabela_selecionada, id_excluir):  
                st.success(f"{tabela_selecionada} excluído com sucesso!")
            else:
                st.error(f"Erro ao excluir {tabela_selecionada}.")
    else:
        st.warning("ID não encontrado.")


def executar_acao(tabela_selecionada, acao_selecionada):
    if acao_selecionada == "Consultar":
        consultar_dados(tabela_selecionada)
    elif acao_selecionada == "Inserir":
        inserir_dados(tabela_selecionada)
    elif acao_selecionada == "Atualizar":
        atualizar_dados(tabela_selecionada)
    elif acao_selecionada == "Excluir":
        excluir_dados(tabela_selecionada)            