import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

def eigenvalue(A, v):
    val = A @ v / v     # Penggunaan simbol '@' sebagai jalan pintas untuk perkalian matriks
    return val[0]

def svd_dominant_eigen(A, epsilon=0.01):
    # Mengembalikan nilai eigenvalue dominan dan eigenvektor dominan dari matriks A
    n, m = A.shape
    k=min(n,m)
    v = np.ones(k) / np.sqrt(k)
    if n > m:
        A = A.T @ A
    elif n < m:
        A = A @ A.T
    
    ev = eigenvalue(A, v)

    while True:
        Av = A @ v
        v_new = Av / np.linalg.norm(Av)
        ev_new = eigenvalue(A, v_new)
        if np.abs(ev - ev_new) < epsilon:
            break

        v = v_new
        ev = ev_new

    return ev_new, v_new

def svd(A, k=None, epsilon=1e-10):
    # Mengembalikan sebanyak k eigenvalue dominan dan eigenvektor dari matriks A
    A = np.array(A, dtype=float)
    n, m = A.shape
        
    svd_so_far = []
    if k is None:
        k = min(n, m)

    for i in range(k):
        matrix_for_1d = A.copy()

        for singular_value, u, v in svd_so_far[:i]:
            matrix_for_1d -= singular_value * np.outer(u, v)

        if n > m:
            _, v = svd_dominant_eigen(matrix_for_1d, epsilon=epsilon)  # vektor singular berikutnya
            u_unnormalized = A @ v
            sigma = np.linalg.norm(u_unnormalized)  # singular value berikutnya
            u = u_unnormalized / sigma
        else:
            _, u = svd_dominant_eigen(matrix_for_1d, epsilon=epsilon)  # vektor singular berikutnya
            v_unnormalized = A.T @ u
            sigma = np.linalg.norm(v_unnormalized)  # singular value berikutnya
            v = v_unnormalized / sigma

        svd_so_far.append((sigma, u, v))

    singular_values, us, vs = [np.array(x) for x in zip(*svd_so_far)]
    return us.T, singular_values, vs
