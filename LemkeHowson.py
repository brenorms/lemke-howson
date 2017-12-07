from Matriz import Matriz
import sys

def criarTabelaAuxiliar(matriz1, matriz2):
	numeroEstrategias = matriz1.getLinhas()+matriz2.getLinhas()

	# numeroEstrategias de linhas, uma linha para cada variavel de slack
	# primeira coluna tem os ids da base e a segunda tem o alpha
	tabela = Matriz.Matriz(numeroEstrategias, numeroEstrategias+2)

	for i in range(0, tabela.getLinhas()):
		tabela.setValor(i, 0, -i) # variavel de slack (negativo)
		tabela.setValor(i, 1, 1) # variavel da base
	return tabela

def equilibrium(tabela, numeroEstrategias):
	raise NotImplementedError

def pivot(tabela, numeroEstrategias, variavelEntrando):
	raise NotImplementedError


def lemkeHowson(matriz1, matriz2):
	raise NotImplementedError

	primeiraVariavelBase = 1
	numeroEstrategias = matriz1.getLinhas()
	variavelBase = pivot()
	while abs(variavelBase) != primeiraVariavelBase:
		variavelBase = pivot(tabela, numeroEstrategias, -variavelBase)

	return equilibrium(tabela, numeroEstrategias)

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