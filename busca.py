# implementando busca entre os arquivos externos

class Buscar_aluno():
    def __init__(self, filename='banco_de_dados_aluno'):
        self.filename = filename

    def localizar_aluno(self, nome_parcial):
        pesquisa_aluno = []
        try:
            with open(self.filename, 'r') as arquivo:

                for linha in arquivo:
                    nome, _, _ = linha.split(',', 2)
                    if nome_parcial.lower() in nome.lower():
                        pesquisa_aluno.append(nome)

        except FileNotFoundError:
            print(f"Erro! {arquivo} não encontrado.")

        except Exception as e:
            print(f"Erro ao ler arquivo {e}")

        return pesquisa_aluno

class Buscar_professor():
    def __init__(self, filename='banco_de_dados_professores'):
        self.filename = filename

    def localizar_aluno(self, nome_parcial):
        pesquisa_professor = []
        try:
            with open(self.filename, 'r') as arquivo:

                for linha in arquivo:
                    nome, _, _ = linha.split(',', 2)
                    if nome_parcial.lower() in nome.lower():
                        pesquisa_professor.append(nome)

        except FileNotFoundError:
            print(f"Erro! {arquivo} não encontrado.")

        except Exception as e:
            print(f"Erro ao ler arquivo {e}")

        return pesquisa_professor