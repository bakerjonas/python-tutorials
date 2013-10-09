import os

def make_matrix(n):
    M = []
    for i in range(n):
        M.append(range(n))
        for j in range(n):
            M[i][j] = float(i + j)
    return M

def matmul_lists(A, B):
    C = []
    n = len(A[0])
    for i in range(n):
        C.append(range(n))
        for j in range(n):
            cij = 0
            for k in range(n):
                 cij += A[i][k]*B[k][j]
            C[i][j] = cij
    return C

A = make_matrix(500)
B = [[float(i+j) for j in range(500)] for i in range(500)]

t0 = os.times()[0]
matmul_lists(A, B)
print "t(dot):", os.times()[0] - t0

