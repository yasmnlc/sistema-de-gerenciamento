from sistema.app import configurar_pagina, selecionar_tabela_acao, executar_acao

def main():
    configurar_pagina()

    tabela_selecionada, acao_selecionada = selecionar_tabela_acao()

    if tabela_selecionada and acao_selecionada:
        executar_acao(tabela_selecionada, acao_selecionada)

if __name__ == "__main__":
    main()