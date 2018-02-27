'''
(int,int,valor) -> matriz (lista de listas)
Cria e retorna uma matriz com num_linhas linhas e num_colunas
colunas em que cada elemento é igual ao valor dado.
'''

def cria_matriz(num_linhas, num_colunas, valor):
    matriz = [] #lista vazia
    for i in range(num_linhas):
        #cria a linha i
        linha = [] #lista vazia
        for j in range(num_colunas):
            valor = int(input("Digite o elemento[" + str(i) + "][" + str(j) + "]"))
            linha.append(valor)


        # adiciona linha a matriz
        matriz .append(linha)

    return matriz

def le_matriz():
    lin = int(input("Digite o numero de linhas da matriz: "))
    col = int(input("Digite o numero de colunas da matriz: "))
    cria_matriz(lin, col)
    return cria_matriz(lin, col)
