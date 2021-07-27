import numpy as np

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

def compress_img(img, k):
    print("Memproses...")
    # Membagi array menjadi tiga buah array 2 dimensi
    r = img[:,:,0]  # array untuk R
    g = img[:,:,1]  # array untuk G
    b = img[:,:,2] # array untuk B
    
    print("Mengompresi gambar...")
    
    # Hitung komponen svd dari ketiga array di atas
    ur,sr,vr = svd(r,k=k)
    ug,sg,vg = svd(g,k=k)
    ub,sb,vb = svd(b,k=k)
    
    # Proses pembentukan compressed image dengan informasi yang lebih sedikit

    # Kita hanya akan memilih sejumlah k singular value dari setiap array untuk membuat suatu gambar yang
    # meng-exclude beberapa informasi dari gambar asli dengan dimensi yang sama
    
    # ur (mxk), diag(sr)(kxk) dan vr (kxn) if image is off (mxn)
    # Asumsikan kita hanya memilih k1 singular value dari diag(sr) untuk membentuk gambar kompresi
    
    rr = np.dot(ur[:,:k],np.dot(np.diag(sr[:k]), vr[:k,:]))
    rg = np.dot(ug[:,:k],np.dot(np.diag(sg[:k]), vg[:k,:]))
    rb = np.dot(ub[:,:k],np.dot(np.diag(sb[:k]), vb[:k,:]))
    
    print("Menyusun gambar hasil kompresi...")
    
    # Membuat array berisi nol yang dimensinya sama seperti matriks gambar asli
    rimg = np.zeros(img.shape)
    
    # Tambahkan matriks untuk r, g, dan b pada array yang telah dibuat
    rimg[:,:,0] = rr
    rimg[:,:,1] = rg
    rimg[:,:,2] = rb
    
    # Jika ada sebuah nilai yang lebih kecil dari 0, nilai tersebut akan dikonversi menjadi nilai mutlaknya
    # Jika ada nilai yang lebih besar dari 255, nilai tersebut akan dikonversi ke 255
    # Hal ini dilakukan karena array uint8 hanya mempunyai nilai antara 0 dan 255
    for ind1, row in enumerate(rimg):
        for ind2, col in enumerate(row):
            for ind3, value in enumerate(col):
                if value < 0:
                    rimg[ind1,ind2,ind3] = abs(value)
                if value > 255:
                    rimg[ind1,ind2,ind3] = 255

    # Konversi array gambar yang telah dikompresi menjadi tipe uint8
    # agar dapat diubah nantinya menjadi objek gambar
    compressed_image = rimg.astype(np.uint8)

    # Konversi array menjadi objek gambar
    compressed_image = Image.fromarray(compressed_image)

    return compressed_image
