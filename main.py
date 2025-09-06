# Mengimpor module utils.py
import utils

# Mendeklarasikan garis untuk memisahkan proses yang sedang berjalan
garis = '=' * 25

# Mencetak ucapan selamat datang
print(garis)
print("Selamat datang di konversi suhu!")
print(garis)

nilai_input = float(input("Masukkan nilai suhu yang akan anda konversi (misal 100): "))
dari_input = input("Masukkan asal suhu anda (C/K/F): ").upper()
ke_input = input("Masukkan tujuan suhu ands (C/K/F): ").upper()

utils.start_logic(nilai_input, dari_input, ke_input)