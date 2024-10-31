"""
Script criado em 28/10/2024
Script finalizado em 30/10/2024

@Autor: Thiago Vicente
"""

from openpyxl import Workbook, load_workbook
import os
import shutil
import threading
import time

'''
As funções abaixo foram criadas para gerenciar um banco de dados Excel (xlsx) de forma segura,
incluindo a criação, atualização, monitoramento e backup periódico para evitar problemas com o banco de dados.

Função 1 - `Criar_banco_de_dados`: Cria um diretório e um arquivo de banco de dados se não existirem.
Função 2 - `Criar_backup`: Cria um backup inicial para evitar a perda de dados.
Função 3 - `Atualizar_backup`: Atualiza o backup periodicamente com as últimas informações do banco de dados.
Função 4 - `Verificar_e_recuperar_banco`: Verifica a integridade do banco de dados e restaura a partir do backup em caso de erro.
Função 5 - `monitorar_banco`: Monitora o banco de dados em segundo plano, realizando backup e verificação a cada intervalo de tempo definido.
'''

def Criar_banco_de_dados(diretorio, banco_de_dados):
    # Adiciona a extensão '.xlsx' se não estiver presente
    if not banco_de_dados.endswith('.xlsx'):
        banco_de_dados += '.xlsx'

    # Cria o diretório se não existir
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
        print(f"Diretório '{diretorio}' criado com sucesso.")

    # Define o caminho completo para o banco de dados dentro do diretório
    caminho_arquivo = os.path.join(diretorio, banco_de_dados)

    # Verifica se o arquivo de banco de dados já existe
    if not os.path.exists(caminho_arquivo):
        workbook = Workbook()
        workbook.save(caminho_arquivo)
        print(f"Arquivo de banco de dados '{caminho_arquivo}' criado com sucesso.")

    else:
        print(f"O arquivo de banco de dados '{caminho_arquivo}' já existe.")

    # Cria um backup inicial
    Criar_backup(caminho_arquivo)

    return caminho_arquivo

def Criar_backup(caminho_arquivo):
    # Cria o diretório de backup se não existir
    dir_backup = 'backup'
    if not os.path.exists(dir_backup):
        os.makedirs(dir_backup)

    # Define o caminho completo do arquivo de backup
    caminho_backup = os.path.join(dir_backup, os.path.basename(caminho_arquivo))
    shutil.copy(caminho_arquivo, caminho_backup)
    print(f"Backup criado com sucesso em '{caminho_backup}'")

    return caminho_backup

def Atualizar_backup(caminho_arquivo, caminho_backup):
    # Atualiza o backup com o conteúdo mais recente do banco de dados
    shutil.copy(caminho_arquivo, caminho_backup)
    print(f"Backup atualizado com sucesso em '{caminho_backup}'")

def Verificar_e_recuperar_banco(caminho_arquivo, caminho_backup):
    try:
        # Tenta abrir o banco de dados para verificar a integridade
        load_workbook(caminho_arquivo)
        print("Banco de dados principal está acessível e íntegro.")

    except Exception:
        # Se houver um problema, restaura o banco de dados a partir do backup
        print("Banco de dados principal corrompido ou ausente. Restaurando a partir do backup...")
        shutil.copy(caminho_backup, caminho_arquivo)
        print("Banco de dados restaurado com sucesso a partir do backup.")

def monitorar_banco(caminho_arquivo, intervalo=600):
    # Cria o backup inicial se não houver nenhum
    caminho_backup = Criar_backup(caminho_arquivo)

    # Função de monitoramento em segundo plano
    def monitor():
        while True:
            # Verifica a integridade e restaura se necessário
            Verificar_e_recuperar_banco(caminho_arquivo, caminho_backup)

            # Atualiza o backup
            Atualizar_backup(caminho_arquivo, caminho_backup)

            # Aguarda o próximo intervalo
            time.sleep(intervalo)

    # Inicia o monitoramento em uma nova thread
    threading.Thread(target=monitor, daemon=True).start()

'''
Função para limpar a tela, evitando o excesso de informações exibidas.
Funciona em qualquer sistema operacional.
'''
def Limpar_tela():
    # Recurso para sistemas Unix/OS X
    if os.name == 'posix':
        _ = os.system('clear')
    # Recurso para sistemas Windows
    else:
        _ = os.system('cls')
