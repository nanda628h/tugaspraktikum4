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
