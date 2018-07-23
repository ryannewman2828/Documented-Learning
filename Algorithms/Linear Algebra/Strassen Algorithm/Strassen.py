#!bin/python
# For simplicity of the implementation this assumes square matrix with size being a power of 2


def matrixAdd(A, B, sub = False):
    assert len(A) == len(B)
    assert len(A[0]) == len(B[0])
    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(A[i])):
            if not sub:
                C[i].append(A[i][j] + B[i][j])
            else:
                C[i].append(A[i][j] - B[i][j])
    return C


def strassen(X, Y):
    if len(X) == 1:
        return [[X[0][0] * Y[0][0]]]
    m = len(X) // 2  # under assumption this is fine only.
    A = []
    B = []
    C = []
    D = []
    E = []
    F = []
    G = []
    H = []
    for i in range(m):
        A.append([])
        B.append([])
        C.append([])
        D.append([])
        E.append([])
        F.append([])
        G.append([])
        H.append([])
        for j in range(m):
            A[i].append(X[i][j])
            C[i].append(X[i + m][j])
            B[i].append(X[i][j + m])
            D[i].append(X[i + m][j + m])
            E[i].append(Y[i][j])
            G[i].append(Y[i + m][j])
            F[i].append(Y[i][j + m])
            H[i].append(Y[i + m][j + m])

    M1 = strassen(matrixAdd(A, C), matrixAdd(E, F))
    M2 = strassen(matrixAdd(B, D), matrixAdd(G, H))
    M3 = strassen(matrixAdd(A, D, True), matrixAdd(E, H))
    M4 = strassen(A, matrixAdd(F, H, True))
    M5 = strassen(matrixAdd(C, D), E)
    M6 = strassen(matrixAdd(A, B), H)
    M7 = strassen(D, matrixAdd(G, E, True))
    I = matrixAdd(M2, matrixAdd(M3, matrixAdd(M6, M7), True))
    J = matrixAdd(M4, M6)
    K = matrixAdd(M5, M7)
    L = matrixAdd(M1, matrixAdd(M3, matrixAdd(M4, M5)), True)

    Z = []
    for i in range(len(I)):
        Z.append([])
        Z[i].extend(I[i])
        Z[i].extend(J[i])
    for i in range(len(K)):
        Z.append([])
        Z[i + len(I)].extend(K[i])
        Z[i + len(I)].extend(L[i])
    return Z


A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
B = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

C = [
    [1, 2],
    [3, 4]
]
D = [
    [1, 2],
    [3, 4]
]

print(strassen(A, B))
