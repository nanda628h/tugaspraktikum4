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
