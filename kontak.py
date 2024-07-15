'Berisi kelas kontak untuk menjalankan program kontak'

import dokumen

class Kontak:
    def __init__(self):
        self.kontak = dokumen.membuka_kontak()

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
        dokumen.menyimpan_kontak(isi=self.kontak)