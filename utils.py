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
    else:
        return "PERHATIAN! Masukkan angka atau kode yang valid"
