# Mengimpor module utils.py
import utils

# Mencetak ucapan selamat datang
print(utils.garis)
print("Selamat datang di konversi suhu!")
print(utils.garis)

nilai_input = float(input("Masukkan nilai suhu yang akan anda konversi (misal 100): "))
dari_input = input("Masukkan asal suhu anda (C/K/F): ").upper()
ke_input = input("Masukkan tujuan suhu ands (C/K/F): ").upper()

