"""
Script criado em 28/10/2024
Script atualizado em 21/11/2024

Script: crud_aluno.py

Descrição:
Este script implementa uma classe para manipulação do banco de dados de alunos. 
Ele encapsula as operações básicas de um CRUD (Create, Read, Update, Delete) aplicadas a um sistema de gestão escolar ou curso.

Funcionalidades principais:
1. Herda as funções básicas do script crud.py, reutilizando métodos gerais de manipulação de dados.
2. Carrega o banco de dados e cria um cabeçalho contendo informações inciais, caso seja a primeira vez iniciado
3. Grava informações cadastradas no banco de dados de alunos, incluindo nome, idade e curso.
4. Lê e exibe as informações completa do aluno com base em um nome parcial ou total informado.
5. Permite a atualização de dados existentes, substituindo informações imprecisas ou desatualizadas.
6. Exclui permanentemente do banco de dados as informações do aluno selecionados.
7. Realiza buscas flexíveis por nome parcial, retornando todos os registros correspondentes.

Observações adicionais:
- Todos os dados são armazenados em memória enquanto o programa está em execução.
- Requer implementação consistente do script crud.py para funcionamento adequado.
- Foi projetado para ser reutilizável e integrável com interfaces de usuário (CLI, GUI, etc.).

@Autor: Thiago Vicente
"""

from aluno import Aluno
from crud import Criar_banco_de_dados
from openpyxl import load_workbook


class Bd_Alunos(Aluno):

    # Função 1
    def __init__(self, nome, idade, curso, caminho="banco_de_dados", arquivo="Banco_de_dados.xlsx"):
        super().__init__(nome, idade, curso)
        self.banco_de_dados = Criar_banco_de_dados(caminho, arquivo)
        self.iniciar_planilha()

    # Função 2
    def iniciar_planilha(self):
        try:
            wb = load_workbook(self.banco_de_dados)
            if "Sheet" in  wb.sheetnames and "Alunos" not in wb.sheetnames:
                sheet = wb["Sheet"]
                sheet.title = "Alunos"

                if sheet.max_row == 1:
                    sheet.append(["Nome", "Idade", "Curso"])

            elif "Professores" not in wb.sheetnames:
                sheet = wb.create_sheet("Aluno")
                sheet.append(["Nome", "Idade", "Curso"])

            wb.save(self.banco_de_dados)

        except Exception as erro:
            print(f"Erro ao criar planilha {erro}")

    # função 3
    def gravar_dados_aluno(self):
        if not all({self.nome, self.idade, self.curso}):
            print("Erro: nome, idade e curso são obrigatórios para gravar o aluno.")
            return

        try:
            wb = load_workbook(self.banco_de_dados)
            sheet = wb["Alunos"]
            sheet.append([self.nome, self.idade, self.curso])
            wb.save(self.banco_de_dados)
            print(f"Aluno(a) {self.nome} foi cadastrado(a) com sucesso")

        except FileNotFoundError as erro:
            print(
                f"Erro o arquivo do banco de dados não foi encontrado: {erro}")

        except Exception as erro:
            print(f"Erro ao gravar informações no banco de dados: {erro}")

    # Função 4
    def ler_dados_aluno(self, nome_parcial):
        aluno_encontrados = []

        try:
            wb = load_workbook(self.banco_de_dados)
            sheet = wb["Alunos"]

            for linha in sheet.iter_rows(min_row=2, values_only=True):
                nome, idade, curso = linha

                if nome_parcial.lower() in nome.lower():
                    aluno_encontrados.append(
                        {"Nome": nome, "Idade": idade, "Curso": curso})

            return aluno_encontrados

        except FileNotFoundError as erro:
            print(
                f"Erro o arquivo do banco de dados não foi encontrado. {erro}")
            

        except Exception as erro:
            print(f"Erro ao acessar banco de dados: {erro}")

    # Função 5
    def alterar_dados_aluno(self, nome_atual, novos_dados):
        try:
            wb = load_workbook(self.banco_de_dados)
            sheet = wb["Alunos"]
            atualizado = False

            for linha in sheet.iter_rows(min_row=2):
                if linha[0].value.lower() == nome_atual.lower():
                    linha[0].value = novos_dados.get('Nome', linha[0].value)
                    linha[1].value = novos_dados.get("Idade", linha[1].value)
                    linha[2].value = novos_dados.get("Curso", linha[2].value)
                    atualizado = True
                    break

            if atualizado:
                wb.save(self.banco_de_dados)
                print(f"Dados do aluno {nome_atual} atualizados com sucesso.")
            else:
                print(f"Aluno {nome_atual} não encontrado.")

        except FileNotFoundError as erro:
            print(
                f"Erro o arquivo do banco de dados não foi encontrado. {erro}")

        except Exception as erro:
            print(f"Erro ao atualizar banco de dados: {erro}")

    # Função 6
    def deletar_dados(self, nome_aluno):
        try:
            wb = load_workbook(self.banco_de_dados)
            sheet = wb['Alunos']
            linhas_removidas = []

            for linha in sheet.iter_rows(min_row=2):
                if linha[0].value.lower() != nome_aluno.lower():
                    linhas_removidas.append([celula.value for celula in linha])

            # Limpa planilha e reescreve as linhas restantes
            for _ in range(sheet.max_row - 1):
                sheet.delete_rows(2)

            for linha in linhas_removidas:
                sheet.append(linha)

            wb.save(self.banco_de_dados)
            print(f"Aluno {self.nome} deletado com sucesso")

        except FileNotFoundError as erro:
            print(
                f"Erro o arquivo do banco de dados não foi encontrado. {erro}")

        except Exception as erro:
            print(f"Erro inesperado: {erro}")

    # função 7
    def buscar_dados(self, nome_parcial):
        alunos_encontrados = []

        try:
            wb = load_workbook(self.banco_de_dados)
            sheet = wb['Alunos']

            for linha in sheet.iter_rows(min_row=2, max_col=1):
                nome = linha[0].value

                if nome and nome_parcial.lower() in nome.lower():
                    alunos_encontrados.append(nome)

            return alunos_encontrados


        except FileNotFoundError:
            print("Banco de dados não encontrado")

        except Exception as erro:
            print(f"Erro inesperado: {erro}")
