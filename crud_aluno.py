from aluno import Aluno


# Configurando parâmetros básicos de banco de dados CRUD
class Bd_Alunos(Aluno):
    def __init__(self, nome, idade, curso, data_base='banco_de_dados/banco_de_dados_alunos.txt'):
        super().__init__(nome, idade, curso)
        self.data_base = data_base


# Função para criar novo cadastro de alunos, no banco de dados
    def gravar_dados_aluno(self):
        with open(self.data_base, 'a') as arquivo:
            linha = f"Nome: {self.nome}, Idade: {self.idade}, Curso: {self.curso}\n"
            arquivo.write(linha)

# Função para ler e exibir informações do aluno, no banco de dados
    def ler_dados_alunos(self):
        alunos = []
        try:
            with open(self.data_base, 'r') as arquivo:
                for linha in arquivo:
                    nome, idade, curso = linha.strip().split(',')
                    alunos.append({
                        'Nome': nome.split(":")[1].strip(),
                        'Idade': idade.split(":")[1].strip(),
                        'Curso': curso.split(":")[1].strip()
                    })

                return alunos

        except FileNotFoundError:
            print('Erro! Banco de dados não encontrado.')
            return []

        except Exception as e:
            print(f"Erro ao ler banco de dados: {e}")
            return []

# Função para atualizar informações do aluno, no banco de dados
    def alterar_dados(self, info_aluno, novo_dado):
        try:
            alunos = self.ler_dados_alunos()
            atualizado = False

            with open(self.data_base, 'w') as arquivo:
                for aluno in alunos:
                    if aluno['Nome'].lower() == info_aluno.lower():
                        aluno['Nome'] = novo_dado.get('Nome', aluno['Nome'])
                        aluno['Idade'] = novo_dado.get('Idade', aluno['Idade'])
                        aluno['Curso'] = novo_dado.get('Curso', aluno['Curso'])
                        atualizado = True

                    linha = f"{aluno['Nome']}, {aluno['Idade']}, {aluno['Curso']}\n"
                    arquivo.write(linha)

            if atualizado:
                print(f"Informações do aluno {info_aluno} foram atualizada.")
            else:
                print(f"As informaçoes do aluno {info_aluno} não foi encontrada.")

        except FileNotFoundError:
            print("Erro! Banco de dados não eoncontrado.")

        except Exception as e:
            print(f"Erro ao atualizar dados: {e}")

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

        except FileNotFoundError:
            print("Erro! Banco de dados não eoncontrado.")

        except Exception as e:
            print(f"Erro ao deletar dados: {e}")

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

        except FileNotFoundError:
            print("Erro! Banco de dados não eoncontrado.")
            
        except Exception as e:
            print(f"Erro ao ler arquivo {e}")

        return alunos_localizados
