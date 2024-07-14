def membuka_kontak(path='kontak.txt'):
    try:
        with open(path, 'r') as file:
            kontak = file.readlines()
        return kontak
    except FileNotFoundError:
        return []

def menyimpan_kontak(path='kontak.txt', isi=[]):
    with open(path, 'w') as file:
        file.writelines(isi)

class Kontak:
    def __init__(self, path='kontak.txt'):
        self.path = path
        self.kontak = membuka_kontak(path)

    def melihat_kontak(self):
        print("\nDaftar Kontak")
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. ' + item.strip())
        else:
            print("Kontak kosong")
            return 1

    def menambah_kontak(self):
        print("Tambah Kontak")
        nama = input("Masukkan nama kontak baru: ")
        telepon = input("Masukkan nomor telepon kontak baru: ")
        email = input("Masukkan email kontak baru: ")
        kontak_baru = f'{nama}, {telepon}, {email}' + '\n'
        self.kontak.append(kontak_baru)
        print("Kontak berhasil ditambahkan")

    def menghapus_kontak(self):
        if self.melihat_kontak() == 1:
            return
        else:
            try:
                i_hapus = int(input("Pilih nomor kontak yang akan dihapus: "))
                del self.kontak[i_hapus-1]
                print("Kontak berhasil dihapus")
            except (ValueError, IndexError):
                print("Kontak gagal dihapus. Input yang Anda masukkan salah")

    def keluar_kontak(self):
        menyimpan_kontak(self.path, self.kontak)

kontak_kantor = Kontak()

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
