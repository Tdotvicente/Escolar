from aluno import Aluno
from crud import Criar_banco_de_dados


# Configurando parâmetros básicos de banco de dados CRUD
class Bd_Alunos(Aluno):
    def __init__(self, nome, idade, curso, caminho='banco_de_dados', arqivo='banco_de_dados_aluno.txt'):
        super().__init__(nome, idade, curso)
        self.data_base = Criar_banco_de_dados(caminho, arqivo)

# Função para criar novo cadastro de alunos, no banco de dados
    def gravar_dados_aluno(self):
        try:
            with open(self.data_base, 'a') as arquivo:
                linha = f"Nome: {self.nome}, Idade: {self.idade}, Curso: {self.curso}\n"
                arquivo.write(linha)

        except Exception as erro:
            print(f"Erro ao gravar dados no banco: {erro}")

# Função para ler e exibir informações do aluno, no banco de dados
    def ler_dados_alunos(self, nome_parcial):
        aluno = []
        try:
            with open(self.data_base, 'r') as arquivo:
                for linha in arquivo:

                    # Criando instância para uma pesquisa apenas usando nome do aluno
                    pesquisa_parcial = linha.strip().split(',')
                    nome = pesquisa_parcial[0].split(":")[1].strip()

                    # Adicionando o restante das informações do aluno
                    if nome_parcial.lower() in nome.lower():
                        idade = pesquisa_parcial[1].split(":")[1].strip()
                        curso = pesquisa_parcial[2].split(":")[1].strip()

                        # Exibindo todas as informações
                        aluno.append({
                            'Nome': nome,
                            'Idade': idade,
                            'Curso': curso
                        })

                return aluno

        # Tratamento de erros e exceções
        except FileNotFoundError:
            print('Erro! Banco de dados não encontrado.')
            return []

        except Exception as erro:
            print(f"Erro ao ler banco de dados: {erro}")
            return []

# Função para atualizar informações do aluno, no banco de dados
    def alterar_dados(self, info_aluno, novo_dado):
        try:
            alunos = self.ler_dados_alunos("")
            atualizado = False

            # Abrindo arquivo, em modo escrita 
            with open(self.data_base, 'w') as arquivo:

                # Encontrando aluno correto, pelo nome
                for aluno in alunos:
                    if aluno['Nome'].lower() == info_aluno.lower():

                        # Atualizando dados confore a necessidade
                        aluno['Nome'] = novo_dado.get('Nome', aluno['Nome'])
                        aluno['Idade'] = novo_dado.get('Idade', aluno['Idade'])
                        aluno['Curso'] = novo_dado.get('Curso', aluno['Curso'])
                        atualizado = True

                    # Revisando os novos dados, antes de substitui-los
                    linha = f"Nome: {aluno['Nome']}, Idade: {aluno['Idade']}, Curso: {aluno['Curso']}\n"
                    arquivo.write(linha)

            if atualizado:
                print(f"Informações do aluno {info_aluno} foram atualizada.")
            else:
                print(
                    f"As informaçoes do aluno {info_aluno} não foi encontrada.")

        # Tratametos de erros e excessões
        except FileNotFoundError:
            print("Erro! Banco de dados não encontrado.")

        except Exception as erro:
            print(f"Erro ao atualizar dados: {erro}")

# Excluindo informações do banco de dados de alunos
    def deletar_dados(self, nome_aluno):
        try:
            alunos = self.ler_dados_alunos()
            aluno_encontrado = False

            with open(self.data_base, 'w') as arquivo:
                for aluno in alunos:
                    if aluno['Nome'].lower() != nome_aluno.lower():
                        linha = f"{aluno['Nome']}, {aluno['Idade']}, {aluno['Curso']}\n"
                        arquivo.write(linha)
                    else:
                        aluno_encontrado = True

            if aluno_encontrado:
                print(f"Dados do aluno {nome_aluno} foram deletados.")
            else:
                print(f"Aluno {nome_aluno} não encontrado.")

        # Tratametos de erros e excessões
        except FileNotFoundError:
            print("Erro! Banco de dados não encontrado.")

        except Exception as erro:
            print(f"Erro ao deletar dados: {erro}")

# Buscar informação de um (ou mais) aluno(s)
    def buscar_dados(self, nome_parcial):
        alunos_localizados = []
        try:
            with open(self.data_base, 'r') as arquivo:
                for linha in arquivo:
                    nome, _, _ = linha.strip().split(',', 2)
                    nome = nome.split(":")[1].strip()
                    # Criando uma instancia para pesquisar alunos
                    # com nomes parcial ou total
                    if nome_parcial.lower() in nome.lower():
                        alunos_localizados.append(nome)

        # Tratametos de erros e excessões
        except FileNotFoundError:
            print("Erro! Banco de dados não encontrado.")

        except Exception as erro:
            print(f"Erro ao ler arquivo: {erro}")

        return alunos_localizados
