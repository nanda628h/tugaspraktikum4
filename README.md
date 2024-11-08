# Latihan 1: latihan1.py
1. Tampilkan n bilangan acak yang lebih kecil dari 0.5.
2. nilai n diisi pada saat runtime
3. anda bisa menggunakan kombinasi while dan for untuk menyelesaikannya
4. gunakan fungsi random() yang dapat diimport terlebih dahulu

Membangkitkan nilai random()
from random import random
a = random()
print(a)
![image](https://github.com/user-attachments/assets/e6a1ae5a-cfaa-46e4-a352-234554c1be3c)

# Latihan 2: latihan2.py
Seorang pengusaha menginvestasikan uangnya untuk memulai usahanya dengan modal
awal 100 juta, pada bulan pertama dan kedua belum mendapatkan laba. pada bulan ketiga
baru mulai mendapatkan laba sebesar 1% dan pada bulan ke 5, pendapatan meningkat 5%,
selanjutnya pada bulan ke 8 mengalami penurunan keuntungan sebesar 2%, sehingga laba
menjadi 3%. Hitung total keuntungan selama 8 bulan berjalan usahanya.
![image](https://github.com/user-attachments/assets/ce9c6f94-882b-4ab5-9294-4e5ee6d06282)

# Latihan 3: latihan3.py
Buat program yang mensimulasikan mesin ATM sederhana. Pengguna memiliki saldo awal
sebesar Rp 1.000.000, dan dapat menarik uang hingga saldo habis atau memilih untuk
keluar.

![image](https://github.com/user-attachments/assets/abb79ff7-a140-44e3-b625-c337f6dae7dc)


## Latihan 1
``` python
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

```
## output
![image](https://github.com/user-attachments/assets/980da009-5ae3-4f42-814f-8bbfe438660b)

## Penjelasan Kode:
``` python
Import Modul: from random import random digunakan untuk mengimpor fungsi random() dari modul random, yang memungkinkan kita menghasilkan bilangan acak antara 0 dan 1.
Input: n = int(input("Masukkan jumlah bilangan acak yang diinginkan: ")) meminta pengguna untuk memasukkan jumlah bilangan acak (nilai n) yang diinginkan.
Looping:
Loop while count < n berfungsi untuk memastikan bahwa kita menghasilkan n bilangan acak yang lebih kecil dari 0.5.
Di dalam loop, a = random() menghasilkan bilangan acak baru setiap kali loop dijalankan.
Kondisi dan Pencetakan:
if a < 0.5: memastikan hanya bilangan yang lebih kecil dari 0.5 yang ditampilkan.
Jika bilangan memenuhi kondisi, print(a) menampilkan bilangan tersebut, dan count += 1 menambah penghitung untuk memastikan bahwa kita mendapatkan tepat n bilangan.
```
# Latihan 2
```python
# Modal awal investasi
modal_awal = 100_000_000  # 100 juta rupiah

# Keuntungan per bulan (dalam persentase)
laba_per_bulan = [0, 0, 1, 1, 5, 5, 5, 3]

# Variabel untuk menyimpan total keuntungan
total_keuntungan = 0

# Menghitung keuntungan setiap bulan
for bulan, laba in enumerate(laba_per_bulan, start=1):
    keuntungan_bulan_ini = modal_awal * (laba / 100)
    total_keuntungan += keuntungan_bulan_ini
    print(f"Bulan ke-{bulan}: Laba {laba}%, Keuntungan: Rp{keuntungan_bulan_ini:,.0f}")

# Output total keuntungan selama 8 bulan
print(f"\nTotal keuntungan selama 8 bulan: Rp{total_keuntungan:,.0f}")
```


## Penjelasan Kode:

Modal awal: Disimpan dalam variabel modal_awal.
Laba per bulan: Disimpan dalam list laba_per_bulan, di mana setiap indeks menunjukkan keuntungan (%) untuk setiap bulan.
Perhitungan laba bulanan: Untuk setiap bulan, laba dihitung berdasarkan persentase laba dan modal_awal.
Total keuntungan: Hasil dari setiap bulan dijumlahkan ke dalam variabel total_keuntungan.
Output: Menampilkan keuntungan setiap bulan dan total keuntungan setelah 8 bulan.

# Latihan 3
``` python
# Program simulasi mesin ATM sederhana

# Saldo awal pengguna
saldo = 1_000_000  # Rp 1.000.000

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\n===== Mesin ATM Sederhana =====")
    print("1. Cek Saldo")
    print("2. Tarik Uang")
    print("3. Keluar")

# Fungsi untuk cek saldo
def cek_saldo():
    print(f"Saldo Anda saat ini: Rp {saldo}")

# Fungsi untuk tarik uang
def tarik_uang():
    global saldo
    try:
        jumlah = int(input("Masukkan jumlah yang ingin ditarik: Rp "))
        if jumlah <= 0:
            print("Jumlah harus lebih besar dari nol.")
        elif jumlah > saldo:
            print("Saldo tidak mencukupi.")
        else:
            saldo -= jumlah
            print(f"Anda berhasil menarik Rp {jumlah}. Saldo Anda sekarang: Rp {saldo}")
    except ValueError:
        print("Masukkan angka yang valid.")

# Program utama

while True:
    tampilkan_menu()
    pilihan = input("Pilih opsi (1/2/3): ")

    if pilihan == '1':
        cek_saldo()
    elif pilihan == '2':
        tarik_uang()
    elif pilihan == '3':
        print("Terima kasih telah menggunakan mesin ATM sederhana ini. Selamat tinggal!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
```
## output program
![image](https://github.com/user-attachments/assets/6da5f825-680f-4e32-aac2-993962243d78)

## penjelasan singkat 

Saldo Awal: saldo diset ke Rp 1.000.000.
Fungsi tampilkan_menu: Menampilkan opsi menu untuk pengguna, yaitu cek saldo, tarik uang, atau keluar.
Fungsi cek_saldo: Menampilkan saldo pengguna saat ini.
Fungsi tarik_uang: Mengurangi saldo pengguna sesuai jumlah yang ditarik, dengan validasi untuk memastikan saldo cukup dan jumlah yang ditarik valid.
Loop Utama: Menjalankan program secara terus-menerus hingga pengguna memilih untuk keluar.


