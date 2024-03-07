def hitung_ipk(mata_kuliah):
    total_bobot = 0
    total_sks = 0

    for mk in mata_kuliah:
        nilai = float(input(f"Masukkan nilai untuk mata kuliah {mk['nama']}: "))
        if nilai >= 80:
            bobot = 4
        elif nilai >= 70:
            bobot = 3
        elif nilai >= 60:
            bobot = 2
        elif nilai >= 50:
            bobot = 1
        else:
            bobot = 0
        total_bobot += bobot * mk['sks']
        total_sks += mk['sks']

    if total_sks == 0:
        return 0
    else:
        return total_bobot / total_sks

mata_kuliah = []
for i in range(5):
    nama_matkul = input(f"Masukkan nama mata kuliah ke-{i+1}: ")
    sks = int(input(f"Masukkan SKS untuk mata kuliah {nama_matkul}: "))
    mata_kuliah.append({'nama': nama_matkul, 'sks': sks})

ipk = hitung_ipk(mata_kuliah)
print("IPK Anda adalah :", ipk)
