from os import system, name
import random
import string

def limpa_tela():
	if name == "nt":
		_=system("cls")
	else:
		_=system("clear")

class Senha():

	def __init__(self, quantidade = 6):
		self.quantidade = quantidade

	def numero(self):
		limpa_tela()
		armazem=""
		i = 0
		while i < self.quantidade:
			armazem += str(random.randint(0,9))
			i += 1
		lista_senhas.append(armazem)
		print(f"Senha gerada: {armazem}")

	def numero_letra(self):
		limpa_tela()
		lista_numero_letra = string.ascii_lowercase + string.digits
		lista_caracteres = random.choices(lista_numero_letra, k=self.quantidade)
		lst = ""
		for i in lista_caracteres:
			lst += i
		lista_senhas.append(lst)
		print(lst)

	def numero_letra_maiuscola(self):
		limpa_tela()
		lista_numero_letra = string.ascii_letters + string.digits
		lista_caracteres = random.choices(lista_numero_letra, k=self.quantidade)
		lst = ""
		for i in lista_caracteres:
			lst += i
		lista_senhas.append(lst)
		print(lst)

	def todos_caracteres(self):
		limpa_tela()
		lista_todos_caracteres = string.ascii_letters + string.digits + string.punctuation
		lista_caracteres = random.choices(lista_todos_caracteres, k=self.quantidade)
		lst = ""
		for i in lista_caracteres:
			lst += i
		lista_senhas.append(lst)
		print(lst)


def mostra_senhas(lista_senhas):
	limpa_tela()
	print("-"*20 + "Senhas" + "-"*20)
	for i in lista_senhas:
		print(f"- {i}")
	print("")

lista_senhas = []

def principal():
	while True:
		print("-"*20 + "Gerador de Senhas" + "-"*20)
		print("1- Gerar uma senha")
		print("2- Mostrar senhas geradas")
		print("3- Sair")

		try:
			resposta = int(input("Opção: "))
		except ValueError:
			limpa_tela()
			print("Digito inválido!")
			continue

		if resposta == 1:
			try:
				quantidade_caracter = int(input("Quantidade de caracteres(Max: 32 Min: 1): "))
				if quantidade_caracter <= 0 or quantidade_caracter > 32:
					limpa_tela()
					print("Número inválido!")
					continue
			except ValueError:
				limpa_tela()
				print("Digito inválido!")
				continue
			limpa_tela()
			senha = Senha(quantidade_caracter)
			print("-"*20 + "Tipos de Senhas"+ "-"*20)
			print("1- Números\n2- Números e Letras\n3- Números e Letras(maiusculas e minusculas\n4- Todos os caracteres)")
			try:
				opcao = int(input("Opção: "))
			except ValueError:
				print("Digito inválido!")
				continue
			if opcao == 1:
				senha.numero()
			elif opcao == 2:
				senha.numero_letra()
			elif opcao == 3:
				senha.numero_letra_maiuscola()
			elif opcao == 4:
				senha.todos_caracteres()
			else:
				limpa_tela()
				print("Opção inválida!")

		elif resposta == 2:
			mostra_senhas(lista_senhas)		

		elif resposta == 3:
			break

		else:
			limpa_tela()	
			print("Não há está opção.")
			pass

if __name__ == "__main__":
	limpa_tela()
	principal()