# Mengimpor module utils.py
import utils

# Mendeklarasikan garis untuk memisahkan proses yang sedang berjalan
garis = '=' * 25
garis2 = '-' * 25

# Mencetak ucapan selamat datang
print(garis)
print("Selamat datang di konversi suhu!")
print(garis)

# Membuat perulangan (while) untuk menangani error
while True:
    # Membuat logic try dan except untuk menangani error nilai non-integer untuk variabel nilai
    try:
        nilai = float(input("Masukkan nilai suhu yang akan anda konversi (misal 100): "))
    except ValueError:
        # Mencetak teks 'ERROR: Masukkan angka yang valid' ketika nilai bukan merupakan angka
        print("ERROR: Masukkan angka yang valid")
        print(garis2)
        continue
    
    ''' Menginisialisasi variabel 'dari' dengan input dari pengguna '''
    dari = input("Masukkan asal suhu anda (C/K/F): ").upper()
    
    # Mengecek kondisi nilai tidak boleh negatif jika berasal dari suhu Kelvin
    if dari == "K" and nilai < 0:
        # Mencetak pesan dan garis pembatas jika suhu Kelvin bernilai negatif
        print("ERROR: Suhu kelvin tidak boleh negatif")
        print(garis2)
        continue # Mengulangi perulangan dari atas
    
    # Mengecek kondisi nilai 'dari' harus berisi C, K, F
    if dari not in ["C", "K", "F"] :
        # Mencetak pesan error dan garis pembatas jika user input bukan C, K, atau F
        print("ERROR: Masukkan asal suhu dengan tepat!")
        print(garis2)
        continue # Mengulangi perulangan dari atas
    
    '''Menginialisasi variabel "ke" dengan input dari pengguna'''
    ke = input("Masukkan tujuan suhu ands (C/K/F): ").upper()
    
    # Mengecek kondisi nilai 'ke' harus berisi C, K, F
    if ke not in ["C", "K", "F"]:
        # Mencetak pesan error dan garis pembatas jika user input bukan C, K, atau F
        print("ERROR: Suhu tujuan input anda salah")
        print(garis2)
        continue # Mengulangi perulangan dari atas
    
    '''Menginisialisasi return dari fungsi 'konverensi_suhu' ke dalam variabel 'hasil' dengan hasil input dari pengguna'''
    hasil = utils.konversi_suhu(nilai, dari, ke)
    print(hasil) # mencetak variabel hasil
    
    '''Menginisialisasi variabel 'confirm' dalam menawarkan pengguna untuk melakukan konversi suhu lagi''' 
    confirm = input("Ingin konversi suhu lagi? (Y/N): ").upper()
    
    if confirm == "Y":
        # Mengecek kondisi apakah pengguna menjawab iya
        print(garis, "\n")
        continue # Mengulangi konversi lagi dari atas
    else:
        # Mencetak pesan jika pengguna tidak ingin melakukan konversi lagi
        print("Terimakasih telah mengkonversi suhu! Silahkan datang lagi bila ingin mengonversi suhu lainnya. Stay Safe!")
        
    break

