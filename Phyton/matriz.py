
def main():
    A = leia_matriz()
    if simetrica(A):
        print("Matriz simétrica")
    else:
        print("Matriz não é simétrica")

def leia_matriz():
    nlinhas  = int(input("Digite o número de linhas: "))
    ncolunas = int(input("Digite o número de colunas: "))
    matriz = []
    for i in range(nlinhas):
        linha = []
        for j in range(ncolunas):
            num = int(input("Digite elem (%d,%d): "%(i,j)))
            linha.append(num)
        matriz.append(linha)
    return matriz

def simetrica(matriz):
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])
    if nlinhas != ncolunas:
        return False
    for i in range(nlinhas):
        for j in range(i):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

main()