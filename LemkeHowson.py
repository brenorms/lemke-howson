# -*- coding: UTF-8 -*-

from __future__ import division #wow
from Matriz import Matriz
import sys
import pprint
import numpy

def criarTabelaAuxiliar(matriz1, matriz2):
	if matriz1.getLinhas() != matriz2.getLinhas() or matriz1.getColunas() != matriz2.getColunas():
		raise ValueError, 'As matrizes tẽm tamanhos diferentes.'

	numeroEstrategias = matriz1.getLinhas()+matriz2.getColunas()

	# numeroEstrategias de linhas, uma linha para cada variavel de slack
	# primeira coluna tem os ids da base e a segunda tem o alpha
	tabela = Matriz(numeroEstrategias, numeroEstrategias+2)

	for i in range(0, tabela.getLinhas()):
		tabela.setValor(i, 0, -i) # variavel de slack (negativo)
		tabela.setValor(i, 1, 1) # variavel da base

	for i in range(0, matriz1.getLinhas()):
		for j in range(0, matriz1.getColunas()):
			tabela.setValor(i, matriz1.getLinhas()+j+2, -matriz1.getValor(i, j))

	for i in range(0, matriz2.getLinhas()):
		for j in range(0, matriz2.getColunas()):
			tabela.setValor(j+matriz1.getLinhas(), i+2, -matriz2.getValor(i, j))

	return tabela

def equilibrium(tabela, numeroEstrategias):
	equilibrio = tabela.getLinhas()*[0]
	for i in range(0, tabela.getLinhas()):
		estrategia = tabela.getValor(i, 0)
		probabilidade = tabela.getValor(i, 1)
		equilibrio[abs(estrategia)] = 0 if estrategia<0 or probabilidade<0 else probabilidade
	return (equilibrio[0:numeroEstrategias] , equilibrio[numeroEstrategias:])

def pivot(tabela, numeroEstrategias, variavelEntrando):
	#if variavelEntrando==0:
	#	raise ValueError, 'Variável de entrada inválida.'
	if numeroEstrategias<0 or numeroEstrategias>=tabela.getLinhas():
		raise ValueError, 'Número de estratégias inválido.'
	menorRazao = None
	variavelSaindo = None
	linhaVariavelSaindo = None
	coeficiente = None
	if -numeroEstrategias<=variavelEntrando<0 or numeroEstrategias<=variavelEntrando:
		listaDeLinhasDaVariavel = range(0, numeroEstrategias)
	else:
		listaDeLinhasDaVariavel = range(numeroEstrategias, tabela.getLinhas())
	for i in listaDeLinhasDaVariavel:
		if tabela.getValor(i, 2+abs(variavelEntrando))<0:
			razao = tabela.getValor(i, 2+abs(variavelEntrando))/tabela.getValor(i, 1)
			if menorRazao == None or razao < menorRazao:
				menorRazao = razao
				variavelSaindo = tabela.getValor(i, 0)
				linhaVariavelSaindo = i
				coeficiente = tabela.getValor(i, 2+abs(variavelEntrando))
	#escolheu a variavel que sai
	tabela.setValor(linhaVariavelSaindo, 0, variavelEntrando)
	tabela.setValor(linhaVariavelSaindo, 2+abs(variavelEntrando), 0)
	tabela.setValor(linhaVariavelSaindo, 2+abs(variavelSaindo), -1)
	for i in range(1, tabela.getColunas()):
		novoValor = tabela.getValor(linhaVariavelSaindo, i)/abs(coeficiente)
		tabela.setValor(linhaVariavelSaindo, i, novoValor)

	for i in listaDeLinhasDaVariavel:
		if tabela.getValor(i, 2+abs(variavelEntrando)) != 0:
			for j in range(1, tabela.getColunas()):
				
				novoValor = tabela.getValor(i, j) + tabela.getValor(i, 2+abs(variavelEntrando)) * tabela.getValor(linhaVariavelSaindo, j)
				tabela.setValor(i, j, novoValor)
			tabela.setValor(i, 2+abs(variavelEntrando), 0)
	return variavelSaindo

def normalizar(equilibrio):
	s = sum(equilibrio)
	norm = [float(i)/s for i in equilibrio]
	return norm

def lemkeHowson(matriz1, matriz2):

	tabela = criarTabelaAuxiliar(matriz1, matriz2)

	primeiraVariavelBase = 1
	numeroEstrategias = matriz1.getLinhas()
	variavelBase = pivot(tabela, numeroEstrategias, primeiraVariavelBase)
	while abs(variavelBase) != primeiraVariavelBase:
		variavelBase = pivot(tabela, numeroEstrategias, -variavelBase)
	eq = equilibrium(tabela, numeroEstrategias)
	return (normalizar(eq[0]), normalizar(eq[1]))

def main(arquivoJogador1, arquivoJogador2):
	with open(arquivoJogador1, 'r') as fin:
		textoJogador1 = fin.read()
	with open(arquivoJogador2, 'r') as fin:
		textoJogador2 = fin.read()

	matrizJogador1 = Matriz.criarMatrizPorTexto(textoJogador1, int)
	matrizJogador2 = Matriz.criarMatrizPorTexto(textoJogador2, int)

	print 'Matriz do Jogador 1:\n'
	print matrizJogador1
	print '\nMatriz do Jogador 2:\n'
	print matrizJogador2
	res = lemkeHowson(matrizJogador1, matrizJogador2)
	print '\nEquilíbrio de Nash:\n'
	pprint.pprint (res)



if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])