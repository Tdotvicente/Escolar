"""
Script criado em 28/10/2024
Script atualizado em /11/2024

@Autor: Thiago Vicente
"""

from professor import Professor
from crud import Criar_banco_de_dados
from openpyxl import load_workbook


# Carrecando informações basicas dentro do script
class Bd_professores(Professor):
    def __init__(self, nome, idade, disciplina, caminho="banco_de_dados", arquivo="Banco_de_dados.xlsx"):
        super().__init__(nome, idade, disciplina)
        self.banco_de_dados = Criar_banco_de_dados(caminho, arquivo)
        self.iniciar_planilha()

    # Inicializa uma planilha com cabeçalhos, se a mesma estiver vazia
    def iniciar_planilha(self):
        try:
            wb = load_workbook(self.banco_de_dados)
            sheet = wb["Professores"]

            # Verificando o cabeçalho está configurado
            if sheet.max_row == 1 and sheet.cell(row=1, column=1).value is None:
                sheet.append(["Nome", "Idade", "Disciplina"])
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
        professores_encontrados = self.ler_dados_professor(nome_parcial)
        return [professor["Nome"] for professor in professores_encontrados]