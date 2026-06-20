import os

# Nama file menggunakan ekstensi .txt untuk kemudahan membaca teks biasa
NAMA_FILE = 'kontak.txt' 

# ==========================================
# FUNGSI ALGORITMA PENGURUTAN (QUICK SORT)
# ==========================================

def quickSort(data):
    # Memanggil fungsi dengan indeks awal 0 dan indeks akhir
    quickSortHelper(data, 0, len(data)-1)

def quickSortHelper(data, first, last):
    if first < last:
        # Mencari titik pisah atau splitpoint menggunakan fungsi partition
        splitpoint = partition(data, first, last)
        
        # Mengurutkan bagian kiri dari splitpoint secara rekursif
        quickSortHelper(data, first, splitpoint-1)
        # Mengurutkan bagian kanan dari splitpoint secara rekursif
        quickSortHelper(data, splitpoint+1, last)

def partition(data, first, last):
    # Patokan atau acuan diambil dari "Nama" pada elemen indeks pertama
    # data[first] adalah tuple ('Nama', 'Nomor'), jadi kita ambil [0]-nya
    acuan = data[first][0]

    leftmark = first + 1
    rightmark = last
    done = False

    while not done:
        # leftmark bergerak ke kanan selama namanya <= patokan
        while leftmark <= rightmark and data[leftmark][0] <= acuan:
            leftmark = leftmark + 1

        # rightmark bergerak ke kiri selama namanya >= patokan
        while data[rightmark][0] >= acuan and rightmark >= leftmark:
            rightmark = rightmark - 1

        # Jika kedua penunjuk saling melewati, partisi selesai
        if rightmark < leftmark:
            done = True
        else:
            # Swap elemen utuh (Nama beserta Nomor) di leftmark dan rightmark
            temp = data[leftmark]
            data[leftmark] = data[rightmark]
            data[rightmark] = temp

    # Kembalikan elemen acuan ke posisi tengah yang tepat di rightmark
    temp = data[first]
    data[first] = data[rightmark]
    data[rightmark] = temp

    return rightmark

# ==========================================
# FUNGSI MANAJEMEN FILE TXT
# ==========================================

def muat_data():
    data = {}
    # Mengecek apakah file TXT sudah ada sebelumnya
    if os.path.exists(NAMA_FILE): 
        # Membuka file mode 'r' (read) untuk membaca data
        with open(NAMA_FILE, 'r') as file:
            for line in file:
                if ',' in line:
                    # Memisahkan baris teks menjadi 'nama' dan 'nomor' menggunakan koma
                    nama, nomor = line.strip().split(',', 1)
                    data[nama] = nomor 
    return data

def simpan_data(data):
    list_kontak = list(data.items())
    
    # Memanggil fungsi quick sort (data list_kontak akan langsung terurut secara otomatis)
    quickSort(list_kontak)
    
    with open(NAMA_FILE, 'w') as file: 
        for nama, nomor in list_kontak:
            file.write(f"{nama},{nomor}\n")
            
    data.clear()
    for nama, nomor in list_kontak:
        data[nama] = nomor
        
    print("\nMantap! Data berhasil diurutkan (A-Z) dan disimpan permanen ke kontak.txt.")

# ==========================================
# APLIKASI CRUD: BUKU TELEPON PINTAR
# ==========================================

# Memuat data ke memori saat program pertama kali dijalankan
daftar = muat_data() 

def tambah_kontak():
    print("\n--- TAMBAH KONTAK BARU ---") 
    # .title() memastikan huruf pertama setiap kata kapital (misal: "budi" -> "Budi")
    nama = input("Masukkan Nama: ").title()
    
    if nama in daftar: 
        print(f"Eitsss! Kontak dengan nama '{nama}' sudah ada.") 
    else: 
        nomor = input("Masukkan Nomor Telepon: ") 
        # Menambahkan data baru (key: nama, value: nomor) ke dalam dictionary
        daftar[nama] = nomor 
        print(f"Kontak '{nama}' berhasil ditambah (Pilih menu 6 untuk simpan permanen!).") 

def lihat_kontak(): 
    print("\n--- DAFTAR KONTAK ---") 
    if not daftar: 
        print("Buku telepon masih kosong.") 
    else:
        # Looping untuk menampilkan seluruh isi dictionary
        for nama, nomor in daftar.items(): 
            print(f" Nama: {nama} \t| Nomor: {nomor}") 

def cari_kontak(): 
    print("\n--- CARI KONTAK ---") 
    print("1. Cari berdasarkan Nama") 
    print("2. Cari berdasarkan Nomor") 
    opsi = input("Pilih metode pencarian (1/2): ") 

    ditemukan = False 
    
    if opsi == '1': 
        # Mengubah input ke title case untuk mencocokkan dengan format data
        kata_kunci = input("Masukkan Nama yang dicari: ").title()
        for nama, nomor in daftar.items(): 
            # Pencarian substring (mencari apakah kata kunci ada di dalam nama kontak)
            if kata_kunci.lower() in nama.lower(): 
                print(f" Ketemu! -> Nama: {nama} \t| Nomor: {nomor}") 
                ditemukan = True 
                
    elif opsi == '2': 
        kata_kunci = input("Masukkan Nomor yang dicari: ") 
        for nama, nomor in daftar.items(): 
            if kata_kunci in nomor: 
                print(f" Ketemu! -> Nama: {nama} \t| Nomor: {nomor}") 
                ditemukan = True 
          
    else: 
        print("Pilihan tidak valid.")
        return 
        
    if not ditemukan: 
        print("Tidak ada kontak yang cocok dengan pencarianmu.")

def update_kontak(): 
    print("\n--- UPDATE KONTAK ---") 
    nama_lama = input("Masukkan Nama kontak yang ingin diubah: ").title() 
    
    # Mengecek apakah kontak yang ingin diubah benar-benar ada di memori
    if nama_lama in daftar: 
        print("1. Ubah Nama saja") 
        print("2. Ubah Nomor saja")
        opsi = input("Pilih bagian yang ingin diubah (1/2): ") 

        if opsi == '1':
            nama_baru = input("Masukkan Nama Baru: ").title() 
            if nama_baru in daftar:
                print(f"Nama '{nama_baru}' sudah digunakan kontak lain.")
            else: 
                # Menyimpan nomor lama, menghapus key lama, dan membuat key baru
                nomor_lama = daftar[nama_lama]
                del daftar[nama_lama] 
                daftar[nama_baru] = nomor_lama
                print(f" Nama '{nama_lama}' berhasil diubah menjadi '{nama_baru}'.") 
                
        elif opsi == '2': 
            nomor_baru = input("Masukkan Nomor Telepon Baru: ") 
            # Meng-overwrite (menimpa) value lama dengan value baru
            daftar[nama_lama] = nomor_baru 
            print(f"Nomor untuk '{nama_lama}' berhasil diperbarui.") 
            
        else: 
            print("Pilihan tidak valid.") 
           
    else: 
        print(f" Kontak '{nama_lama}' tidak ditemukan.") 

def hapus_kontak(): 
    print("\n--- HAPUS KONTAK ---") 
    nama = input("Masukkan Nama kontak yang ingin dihapus: ").title() 
    
    if nama in daftar: 
        # Menghapus key dan value dari dictionary
        del daftar[nama] 
        print(f"Kontak '{nama}' dihapus dari memori (Pilih menu 6 untuk simpan permanen!).") 
    else: 
        print(f" Kontak '{nama}' tidak ditemukan.") 

# ==========================================
# PROGRAM UTAMA (MAIN LOOP)
# ==========================================

def main():
    # Looping tak terbatas sampai dipatahkan oleh perintah 'break'
    while True:
        print("\n=== DATA BUKU TELEPON ===") 
        print("1. Tambah Kontak") 
        print("2. Lihat Kontak") 
        print("3. Cari Kontak") 
        print("4. Update Kontak") 
        print("5. Hapus Kontak") 
        print("6. Simpan Data Manual") 
        print("7. Keluar")
        
        pilihan = input("Pilih menu (1-7): ") 
        
        if pilihan == '1': 
            tambah_kontak() 
        elif pilihan == '2': 
            lihat_kontak() 
        elif pilihan == '3': 
            cari_kontak() 
        elif pilihan == '4': 
            update_kontak()
        elif pilihan == '5': 
            hapus_kontak() 
        elif pilihan == '6': 
            simpan_data(daftar) 
        elif pilihan == '7': 
            print(" Keluar aplikasi. Pastikan kamu sudah menyimpan datamu!") 
            # Menghentikan loop dan keluar dari program
            break 
        else: 
            print("Pilihan tidak valid! Silakan pilih angka 1-7.")

# Menjalankan fungsi main() hanya jika script dieksekusi langsung
if __name__ == "__main__":
    main()
