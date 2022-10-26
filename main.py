import pymysql.cursors
from pessoa import Pessoa

# Conexão com o Banco de Dados
conexao = pymysql.connect(
	host='localhost',
	user='root',
	password='04gabriel30',
	database='pessoas',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor
)

# Verificação de conexão
if conexao:
	# Looping do Sistema
	while True:
		try:
			print('='*100)
			print('CADASTRO DE PESSOAS')

			print('''Opções
			
			1 - Cadastrar Pessoas
			2 - Lista de Cadastros
			3 - Busca Por Id
			4 - Busca Por Nome
			5 - Atualizar Dados
			6 - Encerrar Programa
			''')
			opcao = int(input('Escolha: '))

			# POST dos dados para a tabela
			if opcao == 1:
				while True:
					print('='*100)

					# Entrada dos dados para cadastro

					'''
					Verificar e realizar as trativas de dados
					Verificar sobre o sql inject
					'''

					nome = input('Informe seu nome: ')
					idade = input('Informe sua idade[Somente Números]: ')
					sexo = input('Informe seu sexo[Masculino/Feminino/M/F]: ')
					cidade_natal = input('Informe sua cidade natal: ')
					nome_mae = input('Informe o nome da sua mãe: ')
					nome_pai = input('Informe o nome do seu pai: ')
					nome_irmao1 = input('Informe o nome seu primeiro irmão(ã): ')
					nome_irmao2 = input('Informe o nome seu segundo irmão(ã): ')
					nome_avo1 = input('Informe o nome da sua avó: ')
					nome_avo2 = input('Informe o nome do seu avô: ')

					# Classe para validação dos dados
					pessoa = Pessoa(nome, idade, sexo, cidade_natal, nome_mae, nome_pai, nome_irmao1, nome_irmao2, nome_avo1, nome_avo2)

					with conexao.cursor() as cursor:

						# Query SQL
						comando_sql = "INSERT INTO `tb_pessoa` (" \
						              "`nome`," \
						              "`idade`," \
						              "`sexo`," \
						              "`cidade_natal`," \
						              "`nome_mae`," \
						              "`nome_pai`," \
						              "`nome_irmao1`," \
						              "`nome_irmao2`," \
						              "`nome_avo1`," \
						              "`nome_avo2`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

						# Executa o comando SQL
						cursor.execute(comando_sql, (pessoa.nome, pessoa.idade, pessoa.sexo, pessoa.cidade_natal,
						                             pessoa.nome_mae, pessoa.nome_pai, pessoa.nome_irmao1, pessoa.nome_irmao2,
						                             pessoa.nome_avo1, pessoa.nome_avo2))

						conexao.commit() # Salva as mudanças feitas
						print('Cadastro realizado com sucesso!')

					repeticao = ' '

					while repeticao == ' ' or repeticao == '':
						repeticao = input('Deseja continuar realizando cadastros? Informe uma opção[S/N]: ')

					if repeticao.upper() == 'N':
						break

			# GET dos dados da tabela
			if opcao == 2:
				print('='*100)
				with conexao.cursor() as cursor:
					# Comando SQL a ser executado
					comando_sql = "SELECT * FROM `tb_pessoa`"

					cursor.execute(comando_sql) # Execução do comando
					cadastros = cursor.fetchall() # Resultado da busca

					print('Lista de Cadastros:')
					for cadastro in cadastros:
						print(cadastro)

			# GET dos dados por ID
			if opcao == 3:
				print('='*100)

				id = int(input('Informe o número do id que deseja recuperar os dados: '))

				with conexao.cursor() as cursor:
					# Comando SQL
					comando_sql = "SELECT * FROM `tb_pessoa` WHERE `id` = %s"
					cursor.execute(comando_sql, id) # Execução do comando
					cadastro = cursor.fetchone() # Resultado da busca

					if cadastro:
						print('Resultado da Busca: ')
						print(cadastro)
					else:
						print('Registro não encontrado')

			# GET dos dados por nome do registro
			if opcao == 4:
				print('=' * 100)

				nome_busca = input('Informe o número do id que deseja recuperar os dados: ')

				with conexao.cursor() as cursor:
					# Comando SQL
					comando_sql = "SELECT * FROM `tb_pessoa` WHERE `nome` LIKE %s"
					cursor.execute(comando_sql, nome_busca)  # Execução do comando
					cadastro = cursor.fetchone()  # Resultado da busca

					if cadastro:
						print('Resultado da Busca: ')
						print(cadastro)
					else:
						print('Registro não encontrado')

			# PUT dos dados
			if opcao == 5:
				raise NotImplementedError('Opção ainda não implemetada')

			# Encerramento do programa
			if opcao == 6:
				break

		except Exception as e:
			print(e)

	print('='*100)
	print('FIM DO PROGRAMA!')

else:
	print('Erro ao Realizar Conexão!')