import numpy as np
import time
import os

from PIL import Image
from svd_img_processing import compress_img
# from huffman_coding import huffman_coding

directory = str(input("Masukkan path file : "))

image = Image.open(directory)

base = os.path.basename(image.filename)
filename = os.path.splitext(base)[0]

image.save(f'..\in\{filename}.jpg')
image_array = np.asarray(image)

# print("""
# Pilihan algoritma kompresi :
# 1. Singular Value Decomposition (SVD)
# 2. Huffman Coding
# """)

# valid = False
# while not(valid):
#     option = int(input("Masukkan pilihan algoritma untuk kompresi (1/2) : "))
#     if option == 1 or option == 2:
#         valid = True
#     else:
#         print("Input harus berupa bilangan bulat dalam range 0-512")

# print()

# if option == 1:
valid = False
while not(valid):
    k = int(input("Masukkan besar k untuk kompresi (0-512) : "))
    if k >= 0 and k <= 512:
        valid = True
    else:
        print("Input harus berupa bilangan bulat dalam range 0-512")

print()

start = time.time()

compressed_image = compress_img(image_array, k)

end = time.time()

# else:
#     image_array = np.asarray(image, np.uint8)

#     start = time.time()

#     compressed_image = huffman_coding(image_array)

#     end = time.time()

compressed_image.save(f'..\out\{filename}_compressed.jpg')

original_size = os.path.getsize(f'..\in\{filename}.jpg')
compressed_size = os.path.getsize(f'..\out\{filename}_compressed.jpg')

print(f'\nRuntime program : {end-start:.2f} sekon')
print(f'Ukuran gambar original : {original_size} byte')
print(f'Ukuran gambar hasil kompresi : {compressed_size} byte')
print(f'Rasio ukuran memori gambar : {100*compressed_size/original_size:.2f}%')
