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
			print('=' * 45)
			print('CADASTRO DE PESSOAS')

			print('''Opções
			
			1 - Cadastrar Pessoas
			2 - Lista de Cadastros
			3 - Busca Por Id
			4 - Busca Por Nome
			5 - Busca Personalizada
			6 - Atualizar Dados
			7 - Encerrar Programa
			''')
			opcao = int(input('Escolha: '))

			# PUT dos dados para a tabela
			if opcao == 1:
				while True:
					print('='*45)
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

					pessoa = Pessoa(nome, idade, sexo, cidade_natal, nome_mae, nome_pai, nome_irmao1, nome_irmao2, nome_avo1, nome_avo2)

					with conexao:
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
				print('=' * 45)
				with conexao:
					with conexao.cursor() as cursor:
						comando_sql = "SELECT * FROM `tb_pessoa`"

						cursor.execute(comando_sql)
						cadastros = cursor.fetchall()

						for cadastro in cadastros:
							print(cadastro)

			if opcao == 3:
				raise NotImplementedError('Opção ainda não implemetada')

			if opcao == 4:
				raise NotImplementedError('Opção ainda não implemetada')

			if opcao == 5:
				raise NotImplementedError('Opção ainda não implemetada')

			if opcao == 6:
				raise NotImplementedError('Opção ainda não implemetada')

			if opcao == 7:
				break

		except Exception as e:
			print(e)

	print('FIM DO PROGRAMA!')

else:
	print('Erro ao Realizar Conexão!')