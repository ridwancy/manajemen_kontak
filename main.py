import kontak


def main():
    kontak_kantor = kontak.Kontak()

    while True:
        print("\nMenu Kontak")
        print("1. Daftar Kontak")
        print("2. Tambah Kontak")
        print("3. Menghapus Kontak")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            kontak_kantor.melihat_kontak()
        
        elif pilihan == "2":
            kontak_kantor.menambah_kontak()
            
        elif pilihan == "3":
            kontak_kantor.menghapus_kontak()
            
        elif pilihan == "4":
            kontak_kantor.keluar_kontak()
            break
        
        else:
            print("Anda memasukkan pilihan yang salah. Silahkan coba lagi.")

if __name__ == "__main__":
    main()