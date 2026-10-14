sensor_asap = False
sensor_panas = True

# Model logika
alarm = sensor_asap or sensor_panas

# Output
if alarm:
    print("ALARM BERBUNYI")
else:
    print("Alarm TIDAK berbunyi")


tombol_power = True
listrik = True

# Model logika
komputer = tombol_power and listrik

# Output
if komputer:
    print("Komputer MENYALA")
else:
    print("Komputer TIDAK menyala")


kartu_dikenali = True
pin_benar = True

# Model logika
pintu = kartu_dikenali and pin_benar

# Output
if pintu:
    print("Pintu TERBUKA")
else:
    print("Pintu TERTUTUP")


listrik = True
tombol_start = True

# Model logika
mesin = listrik and tombol_start

# Output
if mesin:
    print("Mesin BEROPERASI")
else:
    print("Mesin TIDAK beroperasi")


jalur_kiri = True
jalur_kanan = False

# Model logika
jalur = jalur_kiri ^ jalur_kanan

# Output
if jalur:
    print("Jalur BERHASIL dipilih")
else:
    print("Jalur TIDAK valid")


otomatis = False
manual = True

# Model logika
mode_kipas = otomatis ^ manual

# Output
if mode_kipas:
    print("Mode kipas BERHASIL dipilih")
else:
    print("Mode kipas TIDAK valid")


sensor_gerak = True
tombol_ditekan = False

# Model logika
lampu = sensor_gerak or tombol_ditekan

# Output
if lampu:
    print("Lampu MENYALA")
else:
    print("Lampu MATI")


kartu_akses = False
izin_guru = True

# Model logika
boleh_masuk = kartu_akses or izin_guru

# Output
if boleh_masuk:
    print("Siswa BOLEH masuk kelas")
else:
    print("Siswa TIDAK boleh masuk kelas")