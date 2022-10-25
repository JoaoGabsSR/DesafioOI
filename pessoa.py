class Pessoa:
	def __init__(self, nome, idade, sexo, cidade_natal, nome_mae, nome_pai, nome_irmao1, nome_irmao2, nome_avo1, nome_avo2):
		self.nome = nome.lower().capitalize()

		if self.validador_idade(idade):
			self.idade = idade
		else:
			self.idade = None

		if self.validador_sexo(sexo):
			self.sexo = sexo.lower().capitalize()
		else:
			self.sexo = None

		self.cidade_natal = cidade_natal.lower().capitalize()
		self.nome_mae = nome_mae.lower().capitalize()
		self.nome_pai = nome_pai.lower().capitalize()
		self.nome_irmao1 = nome_irmao1.lower().capitalize()
		self.nome_irmao2 = nome_irmao2.lower().capitalize()
		self.nome_avo1 = nome_avo1.lower().capitalize()
		self.nome_avo2 = nome_avo2.lower().capitalize()

	def validador_idade(self, idade):
		if idade.isnumeric():
			return True

		return False

	def validador_sexo(self, sexo):
		if sexo.lower() in 'masculino feminino f m':
			return True

		return False
