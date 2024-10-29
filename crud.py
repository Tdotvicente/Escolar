"""
script criado em 28/10/2024
script finalizado em

@Autor: Thiago vicente
"""

from openpyxl import Workbook, load_workbook
import os
import shutil
import threading
import time

'''
As funções abaixo serão feitas para criar, atualizar, monitorar e fazer backup de um banco
de dados excel (xlsx). Evitando assim problemas com o banco de dados

A primeira função do arquivo é focada em criar um diretório e um arquivo. Caso não tenha sido criado,
ele criará o diretório e o banco de dados e emitirá uma mensagem de arquivo criado.
Caso o diretório e o banco de dados existam. Uma mensagem de diretório e arquivo existente será exibida

A segunda função do arquivo é focada em criar um diretório para abrigar o backup do banco de dados e fazer o primeiro backup
Que vai evitar acidentes externos ao banco de dados , fazendo assim uma forma segura de mantê-lo salvo e o seu programa funcional

A terceira função, é parte do módulo da segunda função Onde ela sempre será invocada para fazer o backup e não termos
que repetir o a segunda função inteira, só para poder usar parte do script


'''

def Criar_banco_de_dados(diretório, banco_de_dados):
    # Define a extensão do arquivo
    if not banco_de_dados.endswith('.xlsx'):
        banco_de_dados += '.xlsx'

    if not os.path.exists(diretório):
        os.makedirs(diretório)
        print(f"Diretório '{diretório} criado com sucesso.")

    # Caminho completo para adicionar o banco de dados dentro do diretório
    caminho_arquivo = os.path.join(diretório, banco_de_dados)

    if not os.path.exists(banco_de_dados):
        workbook = Workbook()
        workbook.save(caminho_arquivo)
        print(f"Diretório e arquivo '{caminho_arquivo}' criado com sucesso.")

    else:
        print(f"Diretório e arquivo '{caminho_arquivo}' existente.")

    # Cria uma função espelho inicial
    Criar_backup(caminho_arquivo)

    return caminho_arquivo

def Criar_backup(caminho_arquivo):
    dir_backup = 'backup'
    if not os.path.exists(dir_backup):
        os.makedirs(dir_backup)

    caminho_backup = os.path.join(dir_backup, os.path.basename(caminho_arquivo))
    shutil.copy(caminho_arquivo, caminho_backup)
    print(f"Backup criado com sucesso em '{caminho_backup}'")

    return caminho_backup

def Atualizar_backup(caminho_arquivo, caminho_backup):
    shutil.copy(caminho_arquivo, caminho_backup)
    print(f"Backup criado com sucesso, em '{caminho_backup}'")





'''
Função criada para fazer limpeza dos arquivos evitando o excesso de informação exibida.
Idependende do sistema operacional escolhido, para operar esse programa
'''
def Limpar_tela():
    # Usando recurso em sistema Unix/OS X
    if os.name == 'posix':
        _ = os.system('clear')

    # Usando recurso em sistema Windows
    else:
        _= os.system('cls')