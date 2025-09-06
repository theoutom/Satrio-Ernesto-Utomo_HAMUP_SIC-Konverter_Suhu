import main

# Mendeklarasikan garis untuk memisahkan proses yang sedang berjalan
garis = '=' * 25
garis2 = '-' * 25

# Membuat perulangan (while) untuk menangani error
def konversi_suhu(nilai, dari, ke):
    if dari == "C" and ke == "K":
            hasil = nilai + 273.15
            return hasil
    elif dari == "C" and ke == "F":
        return (nilai * 9/5) + 32
    elif dari == "F" and ke == "C":
        return (nilai - 32) * 5/9
    elif dari == "F" and ke == "K":
        hasil = (nilai - 32) * 5/9 + 273.15
        return hasil
    elif dari == "K" and ke == "C":
        return nilai - 273.15
    elif dari == "K" and ke == "F":
        return (nilai - 273.15) * 9/5 + 32
    
def start_logic(nilai, dari, ke):
    while True:
    # Membuat logic try dan except untuk menangani error nilai non-integer untuk variabel nilai
        try:
            nilai = main.nilai_input
        except ValueError:
            # Mencetak teks 'ERROR: Masukkan angka yang valid' ketika nilai bukan merupakan angka
            print("ERROR: Masukkan angka yang valid")
            print(garis2)
            continue
    
        ''' Menginisialisasi variabel 'dari' dengan input dari pengguna '''
        dari = main.dari_input
    
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
        ke = main.ke_input
    
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
