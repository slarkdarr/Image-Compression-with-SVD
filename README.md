# Image Compression with SVD
Memanfaatkan algoritma Singular Value Decomposition (SVD) untuk kompresi gambar
## Prerequisite
1. <a href="https://www.python.org/downloads/">Python 3.5+</a>
## Cara Penggunaan Program
1. Clone repository ini ke direktori lokal Anda
2. Buka command line (cmd) dan change directory `cd` ke folder "src"
3. Ketik `main.py` pada command line
4. Masukkan path file gambar yang ingin Anda kompresi
5. Masukkan besar k (rank matriks) untuk kompresi gambar (Semakin besar k, semakin bagus gambar yang dihasilkan; 0 <= k <= 512)
6. Tunggu sejenak sampai program selesai untuk mengompresi gambar Anda (Semakin besar k pula, semakin lama program berjalan)
7. Setelah program selesai mengompresi, program akan menyimpan file gambar asli pada folder "in" dan file gambar hasil kompresi pada folder "out"
8. Setelah itu, program juga akan menampilkan lamanya runtime, ukuran gambar asli, ukuran gambar hasil kompresi, dan rasio ukuran kedua gambar tersebut pada command line
## Algoritma Singular Value Decomposition (SVD)
Algoritma SVD merupakan suatu metode faktorisasi atau dekomposisi matriks berukuran m x n menjadi tiga buah matriks, yang biasanya disebut matriks U, S, dan V.
<br>
SVD kurang lebih sama seperti Principal Component Analysis (PCA), tetapi lebih general. Pada PCA, kita mengasumsikan masukan dari algoritma adalah matriks persegi, sedangkan pada SVD, kita tidak memiliki asumsi ini.
<br>
Rumus umum dari SVD adalah sebagai berikut.

<p align="center">
  <img src="https://miro.medium.com/max/318/0*i4rDKIAE0o1ZXtBd.">
</p>

Keterangan :
<br>
A adalah matriks awal berukuran m x n yang akan didekomposisi
<br>
U adalah matriks singular kiri (kolomnya merupakan vektor singular kiri). Matriks U merupakan matriks persegi yang berukuran m x m. Kolom dari matriks U berisi <a href="https://mathworld.wolfram.com/Eigenvector.html">eigenvector</a> dari matriks AA<sup>T</sup>.
<br>
S adalah matriks diagonal berukuran m x n yang pada diagonalnya terdapat <a href="https://mathworld.wolfram.com/Eigenvalue.html">eigenvalue</a> dari matriks AA<sup>T</sup> atau A<sup>T</sup>A (Kedua eigenvalue dari masing-masing matriks ini bernilai sama)
<br>
V adalah matriks singular kanan (kolomnya merupakan vektor singular kanan). Matriks V merupakan matriks persegi pula berukuran n x n yang pada setiap kolomnya berisi eigenvector dari matriks A<sup>T</sup>A

<p align="center">
  <img src="https://miro.medium.com/max/700/1*mo8loFarEKeNeVX49205-g.png">
</p>

Dalam melakukan dekomposisi matriks, algoritma SVD melakukan beberapa langkah berikut.
<br>
- Perubahan basis standar menjadi basis V (menggunakan V<sup>T</sup>)
- Mengaplikasikan transformasi yang dideskripsikan oleh matriks S
- Perubahan dari basis V menjadi basis U. Karena matriks awal A bukan matriks persegi, matriks U tidak dapat memiliki dimensi yang sama dengan matriks V dan kita tidak dapat kembali ke basis standar awal kita)<br>

Langkah-langkah tersebut juga dapat dilihat seperti pada gambar berikut.

<p align="center">
  <img src="https://miro.medium.com/max/700/1*aYM93Vik51P4wr7gCSdd3A.png">
</p>

### Pengaruh *rank* matriks terhadap kualitas gambar
Misal matriks awal A memiliki rank r. Misalnya r kita potong menjadi k (r > k) sehingga matriks U, S, dan V yang baru adalah U<sub>1</sub> (matriks U yang diambil mulai dari kolom 1 sampai k), matriks S<sub>1</sub> (matriks S yang diambil mulai dari kolom 1 sampai k), dan matriks V<sub>1</sub> (matriks V yang diambil mulai dari kolom 1 sampai k).
<br>
Ukuran ketiga citra matriks ini adalah m.k + k.k + n.k = k(m+n+k). Maka, untuk mendapatkan citra matriks yang baru, ketiga matriks (U<sub>1</sub>, S<sub>1</sub>, V<sub>1</sub>) direkonstruksi menjadi citra A<sub>1</sub>.
<br>
Dengan cara ini, maka kita dapat menghitung rasio kompresi CR,
<br>
𝐶𝑅 = 𝑚.𝑛 / 𝑘(𝑚+𝑛+𝑘)
<br>
Dengan ini, kita dapat mengambil kesimpulan bahwa semakin besar rank suatu matriks, maka semakin besar pula ukuran citra yang dihasilkan sehingga dapat dikatakan bahwa rank matriks berbanding lurus dengan kualitas gambar yang dihasilkan.

## Referensi
- https://blog.statsbot.co/singular-value-decomposition-tutorial-52c695315254
- https://towardsdatascience.com/simple-svd-algorithms-13291ad2eef2
- https://www.youtube.com/watch?v=gXbThCXjZFM
<br>
(Alasan penggunaan ketiga website di atas sebagai referensi adalah karena isinya bagus, lengkap, dan mudah pula untuk dipahami bagi saya yang baru belajar tentang SVD)

## Library *Source Code*
- <a href="https://numpy.org/">NumPy</a> (Alasan penggunaan numpy adalah karena tugas ini banyak berhubungan dengan matematika sehingga untuk mempermudah pengerjaan, saya mengimport library ini yang menyediakan beberapa fungsi dan metode untuk perhitungan matematika)
- <a href="https://pillow.readthedocs.io/en/stable/">Pillow</a> (Karena tugas ini berhubungan dengan *image processing*, maka saya mengimport library Pillow untuk mempermudah dalam memproses gambar)
- <a href="https://docs.python.org/3/library/time.html">time</a> (Untuk menghitung runtime program)
- <a href="https://docs.python.org/3/library/os.html">os</a> (Untuk mendeteksi file gambar yang diinput oleh user)
