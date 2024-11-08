from random import random

# Meminta input nilai n dari pengguna
n = int(input("Masukkan jumlah bilangan acak yang diinginkan: "))

# Menginisialisasi variabel penghitung
count = 0

# Memulai loop while untuk menghasilkan n bilangan acak
while count < n:
    a = random()  # Menghasilkan bilangan acak antara 0 dan 1
    if a < 0.5:   # Mengecek apakah bilangan tersebut lebih kecil dari 0.5
        print(a)  # Menampilkan bilangan jika memenuhi syarat
        count += 1  # Menambah penghitung jika kondisi terpenuhi
