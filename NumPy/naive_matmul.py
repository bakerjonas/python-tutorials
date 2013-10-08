import os

def make_matrix(n):
    A = []
    for i in range(n):
        A.append(range(n))
        for j in range(n):
            A[i][j] = i + j
    return A

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
B = make_matrix(500)

t0 = os.times()[0]
matmul_lists(A, B)
print "t(vec):", os.times()[0] - t0


