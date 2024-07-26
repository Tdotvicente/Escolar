from aluno import Aluno
from professor import Professor

# Testando cadastro
professor01 = Professor('Thiago Vicente', 36, 'Programação')
aluno01 = Aluno('Thiago dos Santos', 36, 'Banco de dados')

aluno01.gravar_dados_aluno()
aluno01.consultar_dados_aluno()