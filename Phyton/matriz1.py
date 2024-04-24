def leia_matriz():
    m = int(input("Digite m: "))
    n = int(input("Digite n: "))
    matriz = []
    for i in range(m):
        linha = []
        for j in range(n):
            num = int(input("Digite elem (%d,%d): "%(i,j)))
            linha.append(num)
        matriz.append(linha)
    return matriz

def main():
    A = leia_matriz()
    m = len(A)
    n = len(A[0])
    lin_nulas,col_nulas = 0,0
    for i in range(m):
        zerada = True
        for j in range(n):
            if A[i][j] != 0:
                zerada = False
        if zerada:
            lin_nulas += 1

    for j in range(n):
        zerada = True
        for i in range(m):
            if A[i][j] != 0:
                zerada = False
        if zerada:
            col_nulas += 1

    print("Linhas nulas =",lin_nulas)
    print("Colunas nulas =",col_nulas)

main()