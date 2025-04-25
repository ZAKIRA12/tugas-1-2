
kontak = {}

def tambah_kontak(nama, nomor):
    if nama in kontak:
        print(f"Kontak dengan nama {nama} sudah ada.")
    else:
        kontak[nama] = nomor
        print(f"Kontak {nama} berhasil ditambahkan.")

def hapus_kontak(nama):
    if nama in kontak:
        del kontak[nama]
        print(f"Kontak {nama} berhasil dihapus.")
    else:
        print(f"Kontak dengan nama {nama} tidak ditemukan.")

def cari_kontak(nama):
    if nama in kontak:
        print(f"Nomor telepon {nama}: {kontak[nama]}")
    else:
        print(f"Kontak dengan nama {nama} tidak ditemukan.")

def tampilkan_kontak():
    if kontak:
        print("Daftar Kontak:")
        for nama, nomor in kontak.items():
            print(f"{nama}: {nomor}")
    else:
        print("Tidak ada kontak yang tersimpan.")
        


while True:
    print("\nMenu:")
    print("1. Tambah Kontak")
    print("2. Hapus Kontak")
    print("3. Cari Kontak")
    print("4. Tampilkan Semua Kontak")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1-5): ")
    
    if pilihan == "1":
        nama = input("Masukkan nama: ")
        nomor = input("Masukkan nomor telepon: ")
        tambah_kontak(nama, nomor)
    elif pilihan == "2":
        nama = input("Masukkan nama yang ingin dihapus: ")
        hapus_kontak(nama)
    elif pilihan == "3":
        nama = input("Masukkan nama yang ingin dicari: ")
        cari_kontak(nama)
    elif pilihan == "4":
        tampilkan_kontak()
    elif pilihan == "5":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")