"""
Script criado em 28/10/2024
Script atualizado em 21/11/2024

Script: crud_professpr.py

Descrição:
Este script implementa uma classe para manipulação do banco de dados de alunos. 
Ele encapsula as operações básicas de um CRUD (Create, Read, Update, Delete) aplicadas a um sistema de gestão escolar ou curso.

Funcionalidades principais:
1. Herda as funções básicas do script crud.py, reutilizando métodos gerais de manipulação de dados.
2. Carrega o banco de dados e cria um cabeçalho contendo informações inciais, caso seja a primeira vez iniciado
3. Grava informações cadastradas no banco de dados, incluindo nome, idade e curso.
4. Lê e exibe as informações completa do professor com base em um nome parcial ou total informado.
5. Permite a atualização de dados existentes, substituindo informações imprecisas ou desatualizadas.
6. Exclui permanentemente do banco de dados as informações do professor selecionados.
7. Realiza buscas flexíveis por nome parcial, retornando todos os registros correspondentes.

Observações adicionais:
- Todos os dados são armazenados em memória enquanto o programa está em execução.
- Requer implementação consistente do script crud.py para funcionamento adequado.
- Foi projetado para ser reutilizável e integrável com interfaces de usuário (CLI, GUI, etc.).

@Autor: Thiago Vicente
"""

from professor import Professor
from crud import Criar_banco_de_dados
from openpyxl import load_workbook


# Carrecando informações basicas dentro do script
class Bd_Professores(Professor):
    def __init__(self, nome, idade, disciplina, caminho="banco_de_dados", arquivo="Banco_de_dados.xlsx"):
        super().__init__(nome, idade, disciplina)
        self.banco_de_dados = Criar_banco_de_dados(caminho, arquivo)
        self.iniciar_planilha()

    # Inicializa uma planilha com cabeçalhos, se a mesma estiver vazia
    def iniciar_planilha(self):
        try:
            wb = load_workbook(self.banco_de_dados)
            if "Sheet" in  wb.sheetnames and "Professores" not in wb.sheetnames:
                sheet = wb["Sheet"]
                sheet.title = "Professores"

                if sheet.max_row == 1:
                    sheet.append(["Nome", "Idade", "Disciplinas"])

            elif "Professores" not in wb.sheetnames:
                sheet = wb.create_sheet("Professores")
                sheet.append(["Nome", "Idade", "Disciplinas"])

            wb.save(self.banco_de_dados)

        except Exception as erro:
            print(f"Erro ao criar planilha {erro}")

    # Função para criar e gravar um novo registro de professor no banco de dados
    def gravar_dados_professor(self):
        if not all({self.nome, self.idade, self.disciplina}):
            print("Erro: nome, idade e disciplina são obrigatórios para gravar o professor.")
            return

        try:
            wb = load_workbook(self.banco_de_dados)
            sheet = wb["Professores"]
            sheet.append([self.nome, self.idade, self.disciplina])
            wb.save(self.banco_de_dados)
            print(f"Cadastro do {self.nome} feito com sucesso")

        except FileNotFoundError as erro:
            print(f"Erro o arquivo do banco de dados não foi encontrado. {erro}")

        except Exception as erro:
            print(f"Erro ao gravar informações no banco de dados: {erro}")

    # função para buscar e exibir professores pelo nome parcial
    def ler_dados_professor(self, nome_parcial):
        professor_encontrado = []

        try:
            wb = load_workbook(self.banco_de_dados)
            sheet = wb["Professores"]

            for linha in sheet.iter_rows(min_row=2, values_only=True):
                nome, idade, disciplina = linha

                if nome_parcial.lower() in nome.lower():
                    professor_encontrado.append(
                        {"Nome": nome, "Idade": idade, "Disciplina": disciplina})

            return professor_encontrado

        except FileNotFoundError as erro:
            print(f"Erro o arquivo do banco de dados não foi encontrado. {erro}")
            
        except Exception as erro:
            print(f"Erro ao acessar banco de dados: {erro}")

    # Função focada em atualizar informações de um professor, no banco de dados
    def alterar_dados(self, nome_atual, novos_dados):
        try:
            wb = load_workbook(self.banco_de_dados)
            sheet = wb["Professores"]
            atualizado = False

            for linha in sheet.iter_rows(min_row=2):
                if linha[0].value.lower() == nome_atual.lower():
                    linha[0].value= novos_dados.get('Nome', linha[0].value)
                    linha[1].value = novos_dados.get("Idade", linha[1].value)
                    linha[2].value = novos_dados.get("Disciplina", linha[2].value)
                    atualizado = True
                    break

            if atualizado:
                wb.save(self.banco_de_dados)
                print(f"Dados do professor {nome_atual} atualizados com sucesso.")
            else:
                print(f"Professor {nome_atual} não encontrado.")

        except FileNotFoundError as erro:
            print(f"Erro o arquivo do banco de dados não foi encontrado. {erro}")
            
        except Exception as erro:
            print(f"Erro ao atualizar banco de dados: {erro}")

    # Função focada em excluir informações do professor que se encontra no banco de dados
    def deletar_dados(self, nome_professor):
        try:
            wb = load_workbook(self.banco_de_dados)
            sheet = wb['Professores']
            linhas_removidas = []

            for linha in sheet.iter_rows(min_row=2):
                if linha[0].value.lower() != nome_professor.lower():
                    linhas_removidas.append([celula.value for celula in linha])

            # Limpa planilha e reescreve as linhas restantes
            for _ in range(sheet.max_row -1):
                sheet.delete_rows(2)

            for linha in linhas_removidas:
                sheet.append(linha)

            wb.save(self.banco_de_dados)
            print(f"Professor {self.nome} deletado com sucesso")

        except FileNotFoundError as erro:
            print(f"Erro o arquivo do banco de dados não foi encontrado. {erro}")
            
        except Exception as erro:
            print(f"Erro inesperado: {erro}")

    # função de buscar professor pelo nome parcial onde direfente da função
    # ler dados do professor. Essa só retorna os nomes e não informações completas
    def buscar_dados(self, nome_parcial):
        professores_encontrados = []

        try:
            wb = load_workbook(self.banco_de_dados)
            sheet = wb['Professores']

            for linha in sheet.iter_rows(min_row=2, max_col=1):
                nome = linha[0].value

                if nome and nome_parcial.lower() in nome.lower():
                    professores_encontrados.append(nome)

            return professores_encontrados


        except FileNotFoundError:
            print("Banco de dados não encontrado")

        except Exception as erro:
            print(f"Erro inesperado: {erro}")