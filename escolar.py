from crud_aluno import Bd_Alunos
from crud_professor import Bd_Professores
from crud import Limpar_tela

class Menu_cli(Bd_Alunos, Bd_Professores):
    def __init__(self):
        self.bd_alunos = Bd_Alunos(nome=None, idade=None, curso=None)
        self.bd_professores = Bd_Professores(nome=None, idade=None, disciplina=None)

    # Criando opções para um menu CRUD em CLI
    def mostrar_menu(self):
        while True:
            print("\nMENU ESCOLAR CLI\n")
            print("1. Cadastrar")
            print("2. Ler")
            print("3. Atualizar")
            print("4. Excluir")
            print("5. Buscar")
            print("0. Sair\n")

            menu = input("Escolha uma opção: ")

            # Dentro do menu, haverá um submenu
            if menu == '1':
                self.submenu_cadastrar()
            elif menu == '2':
                self.submenu_ler()
            elif menu == '3':
                self.submenu_atualizar()
            elif menu == '4':
                self.submenu_excluir()
            elif menu == '5':
                self.submenu_buscar()
            elif menu == '0':
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida, tente novamente!")

    # Implementando menu de cadastro
    def submenu_cadastrar(self):

        # Limpa excesso de informação
        Limpar_tela()
        print("Digite A, cadastrar aluno ou digite P, para cadastrar professor")

        submenu = input("Escolha a opção do menu: ")

        # Coletando informação do aluno
        if submenu.lower() == 'a':
            print("Cadastro de Aluno(a)\n")
            nome = input("Nome completo: ")
            idade = input('Idade: ')
            curso = input("Curso desejado: ")
            print()

            # Validando idade do aluno
            if not idade.isdigit():
                print("Idade inválida! Tente novamente")
                return

            # Gravando dados do aluno
            self.bd_alunos.nome = nome
            self.bd_alunos.idade = int(idade)
            self.bd_alunos.curso = curso
            self.bd_alunos.gravar_dados_aluno()
            print()

        # Coletando informação do professor
        elif submenu.lower() == 'p':
            print("Cadastro de professor(a)\n")
            nome = input("Nome completo: ")
            idade = input("Idade: ")
            disciplina = input("Disciplina lecionada: ")
            print()

            # Validando dados do professor
            if not idade.isdigit():
                print("Idade inválida! Tente novamente")
                return

            # Gravando dados do professor
            self.bd_professores.nome = nome
            self.bd_professores.idade = int(idade)
            self.bd_professores.disciplina = disciplina
            self.bd_professores.gravar_dados_professor()
            print()

        else:
            print("Opção inválida! Digite uma opção válida\n")
            return

    # Lendo dados do elemento cadastrado
    def submenu_ler(self):

        #Limpa excesso de informação
        Limpar_tela()
        print("Digite A, ler dados do aluno ou digite P, para ler dados do professor")

        submenu = input("Escolha a opção do menu: ")

        # Lendo informação do aluno
        if submenu.lower() == 'a':
            nome_parcial = input("Digite o nome do aluno: ")
            alunos = self.bd_alunos.ler_dados_alunos(nome_parcial)

            # loop para localizar o aluno selecionado, dentro do banco de dados
            if alunos:
                print("Aluno encontrado!\n")
                for aluno in alunos:
                    print(f"Nome: {aluno['Nome']}")
                    print(f"Idade: {aluno['Idade']}")
                    print(f"Curso: {aluno['Curso']}\n")

            else:
                print("Nenhum aluno encontrado, com esse nome!\n")

        # Lendo informação do professor
        elif submenu.lower() == 'p':
            nome_parcial = input("Digite o nome do professor: ")
            professores = self.bd_professores.ler_dados_professores(nome_parcial)

            #loop para localizar o professor selecionado, dentro do banco de dados
            if professores:
                print("Professor encontrado!\n")
                for professor in professores:
                    print(f"Nome: {professor['Nome']}")
                    print(f"Idade: {professor['Idade']}")
                    print(f"Disciplina: {professor['Disciplina']}\n")

            else:
                print("Nenhum professor encontrado, com esse nome!\n")

        else:
            print("Opção inválida! Digite uma opção válida\n")
            return

    # Atualizando informações
    def submenu_atualizar(self):

        # Limpa excesso de informação
        Limpar_tela()
        print("Digite A para atualizar dados de aluno")
        print("Digite P para atualizar dados do professor")

        submenu = input("Escolha uma opção: ")

        if submenu .lower() == 'a':
            info_aluno = input("Digite o nome do aluno a ser atualizado: ")

            # Passando a informação, contida em 'nome_parcial' a um método
            alunos = self.bd_alunos.ler_dados_alunos(info_aluno)

            # Se aluno for achado
            if alunos:

                # Novos dados para o aluno
                novo_nome = input("Digite o novo nome (ou pressione enter, para manter o atual): ")
                nova_idade = input("Digite a nova idade (ou pressione enter, para manter o atual): ")
                novo_curso = input("Digite o novo curso (ou pressione enter, para manter o atual): ")
                print()

                # Atualizando dicionário
                novo_dado = {}
                if novo_nome:
                    novo_dado['Nome'] = novo_nome
                if nova_idade:
                    # Validando idade do aluno
                    if nova_idade.isdigit():
                        novo_dado['Idade'] = int(nova_idade)
                    else:
                        print('Idade inválida!\n')
                        return
                if novo_curso:
                    novo_dado['Curso'] = novo_curso

                # Chamando função para substituir dados aluno
                self.bd_alunos.alterar_dados(info_aluno, novo_dado)
                print(f"Informação(ões) atualizada(s).\n")

            else:
                print("Aluno não encontrado com esse nome!\n")

        elif submenu.lower() == 'p':
            info_professor = input("Digite o nome o nome do professor a ser atualizado: ")

            # Passando a informação, contida em 'nome_parcial' a um método
            professores = self.bd_professores.ler_dados_professores(info_professor)

            # Se professor for achado
            if professores:

                # Novos dados para o professor
                novo_nome = input("Digite o novo nome (ou pressione enter, para manter o atual): ")
                nova_idade = input("Digite a nova idade (ou pressione enter, para manter a atual): ")
                nova_disciplina = input("Digite a nova disciplina (ou pressione enter, para manter a atual): ")
                print()

                novo_dado = {}
                if novo_nome:
                    novo_dado['Nome'] = novo_nome
                if nova_idade:
                    # Validando idade do professor
                    if nova_idade.isdigit():
                        novo_dado['Idade'] = int(nova_idade)
                    else:
                        print("Idade inválida!\n")
                        return
                if nova_disciplina:
                    novo_dado['Disciplina'] = nova_disciplina

                # Chamando a função para substituir dados do professor
                self.bd_professores.alterar_dados(info_professor, novo_dado)
                print("Informação(ões) atualizada(s)\n")

            # Se o professor não for encontrado
            else:
                print("Professor não encontrado com esse nome!\n")

        else:
            print("Opção inválida! Digite uma opção válida.")
            return

    # apagando a informação
    def submenu_excluir(self):

        # Limpa excesso de informação
        Limpar_tela()
        print("Digite A, para excluir o aluno ou digite P, Para excluir o professor")

        submenu = input("Escolha a opção do menu: ")

        # apagando um aluno e suas informações
        if submenu.lower() == 'a':
            nome_aluno = input("Digite o nome do aluno: ")
            self.bd_alunos.deletar_dados(nome_aluno)
            print("Aluno deletado com sucesso\n")

        # Apagando um professor e suas informações
        elif submenu.lower() == 'p':
            nome_professor = input("Digite o nome do professor: ")
            self.bd_professores.deletar_dados(nome_professor)
            print("Professor deletado com sucesso\n")


        else:
            print("Opção inválida, digite uma opção válida!\n")
            return

    def submenu_buscar(self):

        # Limpa excesso de informação
        Limpar_tela()
        print("Digite A, para aluno ou P, para professor")

        submenu = input("Escolha a opção do menu: ")

        if submenu.lower() == 'a':
            nome_aluno = input("Digite o nome do aluno: ")
            resultado = self.bd_alunos.buscar_dados(nome_aluno)

            # Exibindo o(s) aluno(s) encontrado(s)
            if resultado:
                print("Aluno(s) encontrado(s)!")
                for aluno in resultado:
                    print(aluno)

            else:
                print("Aluno(s) não encontrado(s)\n")

        elif submenu.lower() == 'p':
            nome_professor = input("Digite o(s) nome do(s) professor(es): ")
            resultado = self.bd_professores(nome_professor)

            # Exibindo o(s) professor(s) encontrado(s)
            if resultado:
                print("Aluno(s) encontra(s)!")
                for professor in resultado:
                    print(professor)

            else:
                print("Professor(es) não encontrado(s)!\n")

        else:
            print("Opção inválida! Use uma das opções válidas\n")

def Main():
    menu = Menu_cli()
    menu.mostrar_menu()

if __name__ == "__main__":
    Main()
