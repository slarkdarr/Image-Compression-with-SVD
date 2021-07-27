import numpy as np
import time
import os

from PIL import Image
from img_processing import compress_img

directory = str(input("Masukkan path file : "))

start1 = time.time()

image = Image.open(directory)

base = os.path.basename(image.filename)
filename = os.path.splitext(base)[0]

image.save(f'in\{filename}.jpg')
image_array = np.asarray(image)

end1 = time.time()

valid = False
while not(valid):
    k = int(input("Masukkan besar k untuk kompresi (0-512) : "))
    if k >= 0 and k <= 512:
        valid = True
    else:
        print("Input harus berupa bilangan bulat dalam range 0-512")

print()

start2 = time.time()

compressed_image = compress_img(image_array, k)
compressed_image.save(f'out\{filename}_compressed.jpg')

end2 = time.time()

original_size = os.path.getsize(f'in\{filename}.jpg')
compressed_size = os.path.getsize(f'out\{filename}_compressed.jpg')

print(f'\nRuntime program : {end1-start1 + end2-start2:.2f} sekon')
print(f'Ukuran gambar original : {original_size} byte')
print(f'Ukuran gambar hasil kompresi : {compressed_size} byte')
print(f'Rasio ukuran memori gambar : {100*compressed_size/original_size:.2f}%')
