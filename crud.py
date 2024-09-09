import os

def Criar_banco_de_dados(diretorio, nome_arquivo):

    # Verifica se o diretório foi aberto
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
        print(f"Diretório '{diretorio} criado com sucesso.")

    # Caminho completo para o arquivo dentro do diretório
    caminho_arquivo = os.path.join(diretorio, nome_arquivo)

    # Verificando se o arquivo existe
    if not os.path.exists(caminho_arquivo):
        # Criando arquivo vazio
        with open(caminho_arquivo, 'w') as arquivo:
            print(f"Arquivo '{caminho_arquivo}' criado com sucesso.")

    else:
        print(f"Arquivo '{caminho_arquivo}' existente")

    return caminho_arquivo