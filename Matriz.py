# -*- coding: UTF-8 -*-

class Matriz:
	
	def __init__(self, linhas, colunas):

		if linhas <= 0:
			raise ValueError, 'Número de linhas menor que zero.'
		if colunas <= 0:
			raise ValueError, 'Número de colunas menor que zero.'

		self._linhas = linhas
		self._colunas = colunas

		self._matriz = []
		for i in range (1, self._linhas+1):
			linha = []
			for j in range(1, self._colunas+1):
				linha.append(0)
			self._matriz.append(linha)

	def __repr__(self):
		representacao = ''
		for linha in self._matriz:
			for coluna in linha:
				representacao += coluna.__repr__()
				representacao += ' '
			if linha != self._matriz[-1]:
				representacao += '\n'
		return representacao

	def getLinhas(self):
		return self._linhas

	def getColunas(self):
		return self._colunas

	def getValor(self, linha, coluna):
		if linha<0 or linha>self._linhas:
			raise IndexError, 'Linha fora da matriz.'
		if coluna<0 or coluna>self._colunas:
			raise IndexError, 'Coluna fora da matriz.'

		return self._matriz[linha][coluna]

	def setValor(self, linha, coluna, valor):
		if linha<0 or linha>self._linhas:
			raise IndexError, 'Linha fora da matriz.'
		if coluna<0 or coluna>self._colunas:
			raise IndexError, 'Coluna fora da matriz.'

		self._matriz[linha][coluna] = valor

	@staticmethod
	def criarMatrizPorTexto(texto, funcaoDeCast):
		linhasTexto = texto.split('\n')

		nLinhas = len(linhasTexto)
		nColunas = len(linhasTexto[0].split(' '))
		matriz = Matriz(nLinhas, nColunas)

		try:
			for linha in range(0, nLinhas):
				colunasTexto = linhasTexto[linha].split(' ')
				for coluna in range(0, nColunas):
					item = colunasTexto[coluna]
					matriz.setValor(linha, coluna, funcaoDeCast(item))
		except Exception as e:
			raise e
		return matriz

if __name__ == '__main__':
	mat = Matriz(2, 2)
	mat.setValor(0,0,0)
	mat.setValor(0,1,1)
	mat.setValor(1,0,2)
	mat.setValor(0,1,3)
	print mat