from pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina, data_arquivo='banco_de_dados_professores.txt'):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.data_arquivo = data_arquivo

    def consultar_dados_professor(self):
        print(
            f'Nome: {self.nome} \nIdade: {self.idade} \nDisciplinas: {self.disciplina}')

    def gravar_dados_professores(self):
        with open(self.data_arquivo, 'w') as arquivo:
            linha = f"Nome: {self.nome}, Idade: {self.idade}, Disciplina: {self.disciplina}\n"
            arquivo.write(linha)

    def ler_dados_professores(self):
        try:
            with open(self.data_arquivo, 'r') as arquivo:
                linha = arquivo.readline().split()

                if linha:
                    nome, idade, disciplina = linha.split(',')
                    return {
                        "Nome": nome,
                        "Idade": int(idade),
                        "Disciplina": disciplina
                    }
                return None

        except FileNotFoundError:
            return None