"""
Script criado em 28/10/2024
Script atualizado em 20/11/2024

@Autor: Thiago Vicente
"""

from aluno import Aluno
from crud import Criar_banco_de_dados
from openpyxl import load_workbook


# Carrecando informações basicas dentro do script
class Bd_alunos(Aluno):
    def __init__(self, nome, idade, curso, caminho="banco_de_dados", arquivo="Banco_de_dados.xlsx"):
        super().__init__(nome, idade, curso)
        self.banco_de_dados = Criar_banco_de_dados(caminho, arquivo)
        self.iniciar_planilha()

    # Inicializa uma planilha com cabeçalhos, se a mesma estiver vazia
    def iniciar_planilha(self):
        try:
            wb = load_workbook(self.banco_de_dados)
            sheet = wb["Alunos"]

            # Verificando o cabeçalho está configurado
            if sheet.max_row == 1 and sheet.cell(row=1, column=1).value is None:
                sheet.append(["Nome", "Idade", "Curso"])
                wb.save(self.banco_de_dados)

        except Exception as erro:
            print(f"Erro ao criar planilha {erro}")

    # Função para criar e gravar um novo registro de aluno no banco de dados
    def gravar_dados_aluno(self):
        if not all({self.nome, self.idade, self.curso}):
            print("Erro: nome, idade e curso são obrigatórios para gravar o aluno.")
            return

        try:
            wb = load_workbook(self.banco_de_dados)
            sheet = wb["Alunos"]
            sheet.append([self.nome, self.idade, self.curso])
            wb.save(self.banco_de_dados)
            print(f"Cadastro do {self.nome} feito com sucesso")

        except FileNotFoundError as erro:
            print(f"Erro o arquivo do banco de dados não foi encontrado. {erro}")

        except Exception as erro:
            print(f"Erro ao gravar informações no banco de dados: {erro}")

    # função para buscar e exibir alunos pelo nome parcial
    def ler_dados_aluno(self, nome_parcial):
        alunos_encontrados = []

        try:
            wb = load_workbook(self.banco_de_dados)
            sheet = wb["Alunos"]

            for linha in sheet.iter_rows(min_row=2, values_only=True):
                nome, idade, curso = linha

                if nome_parcial.lower() in nome.lower():
                    alunos_encontrados.append(
                        {"Nome": nome, "Idade": idade, "Curso": curso})

            return alunos_encontrados

        except FileNotFoundError as erro:
            print(f"Erro o arquivo do banco de dados não foi encontrado. {erro}")
            
        except Exception as erro:
            print(f"Erro ao acessar banco de dados: {erro}")

    # Função focada em atualizar informações de um aluno, no banco de dados
    def alterar_dados_aluno(self, nome_atual, novos_dados):
        try:
            wb = load_workbook(self.banco_de_dados)
            sheet = wb["Alunos"]
            atualizado = False

            for linha in sheet.iter_rows(min_row=2):
                if linha[0].value.lower() == nome_atual.lower():
                    linha[0].value= novos_dados.get('Nome', linha[0].value)
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
            print(f"Erro o arquivo do banco de dados não foi encontrado. {erro}")
            
        except Exception as erro:
            print(f"Erro ao atualizar banco de dados: {erro}")

    # Função focada em excluir informações do aluno que se encontra no banco de dados
    def deletar_dados_aluno(self, nome_aluno):
        try:
            wb = load_workbook(self.banco_de_dados)
            sheet = wb['Alunos']
            linhas_removidas = []

            for linha in sheet.iter_rows(min_row=2):
                if linha[0].value.lower() != nome_aluno.lower():
                    linhas_removidas.append([celula.value for celula in linha])

            # Limpa planilha e reescreve as linhas restantes
            for _ in range(sheet.max_row -1):
                sheet.delete_rows(2)

            for linha in linhas_removidas:
                sheet.append(linha)

            wb.save(self.banco_de_dados)
            print(f"Aluno {self.nome} deletado com sucesso")

        except FileNotFoundError as erro:
            print(f"Erro o arquivo do banco de dados não foi encontrado. {erro}")
            
        except Exception as erro:
            print(f"Erro inesperado: {erro}")

    # função de buscar aluno pelo nome parcial onde direfente da função
    # ler dados do aluno. Essa só retorna os nomes e não informações completas
    def buscar_dados_aluno(self, nome_parcial):
        alunos_encontrados = self.ler_dados_alunos(nome_parcial)
        return [aluno["Nome"] for aluno in alunos_encontrados]