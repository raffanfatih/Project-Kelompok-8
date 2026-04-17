import os

NAMA_FILE = 'kontak.txt' 

def muat_data():
    buku_telepon = {}
    if os.path.exists(NAMA_FILE): 
        with open(NAMA_FILE, 'r', encoding="utf-8") as file:
            for baris in file:
                # 1. Hapus enter/spasi di ujung, lalu langsung pecah dengan koma
                data_kontak = baris.strip().split(',')
                
                # 2. Cek apakah list hasil pecahan memiliki tepat 2 elemen (nama dan nomor)
                if len(data_kontak) == 2:
                    nama = data_kontak[0]  # Elemen pertama adalah nama
                    nomor = data_kontak[1] # Elemen kedua adalah nomor
                    buku_telepon[nama] = nomor
    return buku_telepon

def simpan_data(data):

    data_terurut = dict(sorted(data.items()))

    with open(NAMA_FILE, 'w') as file: 
        for nama, nomor in data_terurut.items():
            # Menulis format "Nama,Nomor" ke dalam file TXT
            file.write(f"{nama},{nomor}\n") 

    data.clear()
    data.update(data_terurut)
            
    print("\nMantap! Data berhasil disimpan secara permanen ke file kontak.txt")

# ==========================================
# PROGRAM ...
# ==========================================

buku_telepon = muat_data() 

def tambah_kontak():
    print("\n--- TAMBAH KONTAK BARU ---") 
    nama = input("Masukkan Nama: ").title()
    
    # Validasi agar tidak memakai koma pada nama (karena koma dipakai sebagai pemisah di TXT)
    if ',' in nama:
        print("Eitsss! Nama tidak boleh mengandung tanda koma (,).")
        return

    if nama in buku_telepon: 
        print(f"Eitsss! Kontak dengan nama '{nama}' sudah ada.") 
    else: 
        nomor = input("Masukkan Nomor Telepon: ")
        buku_telepon[nama] = nomor 
        print(f"Kontak '{nama}' berhasil ditambah (Pilih menu 6 untuk simpan permanen!).") 

def lihat_kontak(): 
    print("\n--- DAFTAR KONTAK ---") 
    if not buku_telepon: 
        print("Buku telepon masih kosong.") 
    else:
        for nama, nomor in buku_telepon.items(): 
            print(f" Nama: {nama} \t| Nomor: {nomor}") 

def cari_kontak(): 
    pass

def update_kontak(): 
    pass

def hapus_kontak(): 
    print("\n---  HAPUS KONTAK ---") 
    nama = input("Masukkan Nama kontak yang ingin dihapus: ").title()
    
    if nama in buku_telepon: 
        del buku_telepon[nama] 
        print(f"Kontak '{nama}' dihapus dari memori (Pilih menu 6 untuk simpan permanen!).") 
    else: 
        print(f" Kontak '{nama}' tidak ditemukan.") 

# ==========================================
# PROGRAM UTAMA (MAIN LOOP)
# ==========================================

def main():
    while True:
        print("\n===  DATA BUKU TELEPON  ===") 
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
            simpan_data(buku_telepon) 
        elif pilihan == '7': 
            print(" Keluar aplikasi. Pastikan kamu sudah menyimpan datamu!") 
            break 
        else: 
            print("Pilihan tidak valid! Silakan pilih angka 1-7.")

if __name__ == "__main__":
    main()