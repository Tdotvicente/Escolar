from pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, data_arquivo='banco_de_dados_alunos.txt'):
        super().__init__(nome, idade)
        self.curso = curso
        self.data_arquivo = data_arquivo

    def consultar_dados_aluno(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade} \n{self.curso}")

    def gravar_dados_aluno(self):
        with open(self.data_arquivo, 'w') as arquivo:
            linha = f"Nome: {self.nome}, Idade: {self.idade}, Curso: {self.curso}\n"
            arquivo.write(linha)

    def ler_dados_aluno(self):
        try:
            with open(self.data_arquivo, 'r') as arquivo:
                linha = arquivo.readline().strip()

                if linha:
                    nome, idade, curso = linha.split(',')
                    return {
                        'Nome': nome,
                        'Idade': int(idade),
                        'Curso': curso
                    }
                return None

        except FileNotFoundError:
            return None
