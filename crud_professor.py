from professor import Professor


# Configurando parâmetros básicos de banco de dados CRUD
class Bd_Professores(Professor):
    def __init__(self, nome, idade, disciplina, data_base='banco_de_dados/banco_de_dados_professores.txt'):
        super().__init__(nome, idade, disciplina)
        self.data_base = data_base


# Função para criar novo cadastro de professores, no banco de dados
    def gravar_dados_professor(self):
        with open(self.data_base, 'a') as arquivo:
            linha = f"Nome: {self.nome}, Idade: {self.idade}, Disciplina: {self.disciplina}\n"
            arquivo.write(linha)

# Função para ler e exibir informações do professor, no banco de dados
    def ler_dados_professores(self):
        professores = []
        try:
            with open(self.data_base, 'r') as arquivo:
                for linha in arquivo:
                    nome, idade, disciplina = linha.strip().split(',')
                    professores.append({
                        'Nome': nome.split(":")[1].strip(),
                        'Idade': idade.split(":")[1].strip(),
                        'Disciplina': disciplina.split(":")[1].strip()
                    })

                return professores

        except FileNotFoundError:
            print('Erro! Banco de dados não encontrado.')
            return []

        except Exception as e:
            print(f"Erro ao ler banco de dados: {e}")
            return []

# Função para atualizar informações do professor, no banco de dados
    def alterar_dados(self, info_professor, novo_dado):
        try:
            professores = self.ler_dados_professores()
            atualizado = False

            with open(self.data_base, 'w') as arquivo:
                for professor in professores:
                    if professor['Nome'].lower() == info_professor.lower():
                        professor['Nome'] = novo_dado.get('Nome', professor['Nome'])
                        professor['Idade'] = novo_dado.get('Idade', professor['Idade'])
                        professor['Disciplina'] = novo_dado.get('Disciplina', professor['Disciplina'])
                        atualizado = True

                    linha = f"{professor['Nome']}, {professor['Idade']}, {professor['Disciplina']}\n"
                    arquivo.write(linha)

            if atualizado:
                print(f"Informações do professor {info_professor} foram atualizada.")
            else:
                print(f"As informaçoes do professor {info_professor} não foram encontrada.")

        except FileNotFoundError:
            print("Erro! Banco de dados não eoncontrado.")

        except Exception as e:
            print(f"Erro ao atualizar dados: {e}")

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

        except FileNotFoundError:
            print("Erro! Banco de dados não eoncontrado.")

        except Exception as e:
            print(f"Erro ao deletar dados: {e}")

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

        except FileNotFoundError:
            print("Erro! Banco de dados não eoncontrado.")

        except Exception as e:
            print(f"Erro ao ler arquivo {e}")

        return professores_localizados
