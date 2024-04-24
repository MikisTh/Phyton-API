def cria_matriz(nlinhas, ncolunas, valor):
    matriz = []
    for i in range(nlinhas):
        linha = []
        for j in range(ncolunas):
            linha.append(valor)
        matriz.append(linha)
    return matriz

def leia_matriz():
    nlinhas  = int(input("Digite o número de linhas: "))
    ncolunas = int(input("Digite o número de colunas: "))
    matriz = []
    for i in range(nlinhas):
        linha = []
        for j in range(ncolunas):
            num = float(input("Digite elem (%d,%d): "%(i,j)))
            linha.append(num)
        matriz.append(linha)
    return matriz

def imprima_matriz(matriz):
    nlinhas  = len(matriz)
    ncolunas = len(matriz[0])
    print("Matriz: %d x %d"%(nlinhas,ncolunas))
    for i in range(nlinhas):
        for j in range(ncolunas):
            print("%7.2f"%(matriz[i][j]), end="")
        print()

def main():
    A = leia_matriz()
    B = leia_matriz()
    if len(A[0]) != len(B):
        print("Matrizes incompatíveis")
        return
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    C = cria_matriz(m, p, 0.0)
    for i in range(m):
        for j in range(p):
            C[i][j] = 0.0
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]
    imprima_matriz(C)

main()
