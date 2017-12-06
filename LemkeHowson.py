from Matriz import Matriz
import sys

def pivot():
	raise NotImplementedError

def lemkeHowson(matriz1, matriz2):
	raise NotImplementedError

	primeiraVariavelBase = 1
	variavelBase = pivot()
	while variavelBase != primeiraVariavelBase:
		variavelBase = pivot()

def main(arquivoJogador1, arquivoJogador2):
	with open(arquivoJogador1, 'r') as fin:
		textoJogador1 = fin.read()
	with open(arquivoJogador2, 'r') as fin:
		textoJogador2 = fin.read()

	matrizJogador1 = Matriz.criarMatrizPorTexto(textoJogador1, int)
	matrizJogador2 = Matriz.criarMatrizPorTexto(textoJogador2, int)

	print matrizJogador1
	print matrizJogador2

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])