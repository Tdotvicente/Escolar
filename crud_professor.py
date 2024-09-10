from professor import Professor
from crud import Criar_banco_de_dados

# Configurando parâmetros básicos de banco de dados CRUD
class Bd_Professores(Professor):
    def __init__(self, nome, idade, disciplina, caminho='banco_de_dados', arquivo='banco_de_dados_professor.txt'):
        super().__init__(nome, idade, disciplina)
        self.data_base = Criar_banco_de_dados(caminho, arquivo)

# Função para criar novo cadastro de professores, no banco de dados
    def gravar_dados_professor(self):
        try:
            with open(self.data_base, 'a') as arquivo:
                linha = f"Nome: {self.nome}, Idade: {self.idade}, Disciplina: {self.disciplina}\n"
                arquivo.write(linha)

        except Exception as erro:
            print(f"Erro ao gravar os dados no banco: {erro}")

# Função para ler e exibir informações do professor, no banco de dados
    def ler_dados_professores(self, nome_parcial):
        professores = []
        try:
            with open(self.data_base, 'r') as arquivo:
                for linha in arquivo:

                    # Criando instância para uma pesquisa apenas usando nome do professor
                    pesquisa_parcial = linha.strip().split(',')
                    nome = pesquisa_parcial[0].split(":")[1].strip()

                    # Adicionando o restante das informações do professor
                    if nome_parcial.lower() in nome.lower():
                        idade = pesquisa_parcial[1].split(":")[1].strip()
                        disciplina = pesquisa_parcial[2].split(":")[1].strip()

                        # Exibindo todas as informações
                        professores.append({
                            'Nome': nome,
                            'Idade': idade,
                            'Disciplina': disciplina
                        })

                return professores

        # Tratamento de erros e excessões
        except FileNotFoundError:
            print('Erro! Banco de dados não encontrado.')
            return []

        except Exception as erro:
            print(f"Erro ao ler banco de dados: {erro}")
            return []

# Função para atualizar informações do professor, no banco de dados
    def alterar_dados(self, info_professor, novo_dado):
        try:
            professores = self.ler_dados_professores("")
            atualizado = False

            # Abrir arquivo, para ser sobrescrito
            with open(self.data_base, 'w') as arquivo:
                for professor in professores:

                    # localizando professores atravéz do nome
                    if professor['Nome'].lower() == info_professor.lower():

                        # Alterar as informações do professor localizado
                        professor['Nome'] = novo_dado.get('Nome', professor['Nome'])
                        professor['Idade'] = novo_dado.get('Idade', professor['Idade'])
                        professor['Disciplina'] = novo_dado.get('Disciplina', professor['Disciplina'])
                        atualizado = True

                    # reescrevendo as informações no banco de dados
                    linha = f"Nome: {professor['Nome']}, Idade: {professor['Idade']}, Disciplina: {professor['Disciplina']}\n"
                    arquivo.write(linha)

            if atualizado:
                print(f"Informações do professor {info_professor} foram atualizada.")
            else:
                print(f"As informaçoes do professor {info_professor} não foram encontrada.")

        # Tratamento de erros e exceções
        except FileNotFoundError:
            print("Erro! Banco de dados não encontrado.")

        except Exception as erro:
            print(f"Erro ao atualizar dados: {erro}")

# Excluindo informações do banco de dados de professores
    def deletar_dados(self, nome_professor):
        try:
            professores = self.ler_dados_professores()
            professor_encontrado = False

            with open(self.data_base, 'w') as arquivo:
                for professor in professores:
                    if professor['Nome'].lower() != nome_professor.lower():
                        linha = f"{professor['Nome']}, {professor['Idade']}, {professor['disciplina']}\n"
                        arquivo.write(linha)
                    else:
                        professor_encontrado = True

            if professor_encontrado:
                print(f"Dados do professor {nome_professor} foram deletados.")
            else:
                print(f"Professor {nome_professor} não encontrado.")

        # Tratametos de erros e excessões
        except FileNotFoundError:
            print("Erro! Banco de dados não encontrado.")

        except Exception as erro:
            print(f"Erro ao deletar dados: {erro}")

# Buscar informação de um (ou mais) professores(s)
    def buscar_dados(self, nome_parcial):
        professores_localizados = []
        try:
            with open(self.data_base, 'r') as arquivo:
                for linha in arquivo:
                    nome, _, _ = linha.strip().split(',', 2)
                    nome = nome.split(":")[1].strip()
                    # Criando uma instancia para pesquisar professores
                    # com nomes parcial ou total
                    if nome_parcial.lower() in nome.lower():
                        professores_localizados.append(nome)

        # Tratametos de erros e excessões
        except FileNotFoundError:
            print("Erro! Banco de dados não encontrado.")

        except Exception as erro:
            print(f"Erro ao ler arquivo {erro}")

        return professores_localizados
