"Program Manajemen Kontak"

class Kontak:
  def __init__(self):
    self.kontak =[]

  def melihat_kontak(self):
    print("\nDaftar Kontak")
    if self.kontak:
      for num, item in enumerate(self.kontak, start=1):
        print(f'{num}. {item["nama"]} ({item["telepon"]}, {item["email"]})')
    else:
      print("Kontak kosong")
      return 1
      
  def menambah_kontak(self):
    print("Tambah Kontak")
    nama = input("Masukkan nama kontak baru: ")
    telepon = input("Masukkan nomor telepon kontak baru: ")
    email = input("Masukkan email kontak baru: ")
    kontak_baru = {'nama': nama, 'telepon': telepon, 'email': email}
    self.kontak.append(kontak_baru)
    print("Kontak berhasil ditambahkan")
    
  def menghapus_kontak(self):
    if self.melihat_kontak() == 1:
      return
    else:
      i_hapus = int(input("Pilih nomor kontak yang akan dihapus: "))
      del self.kontak[i_hapus-1]
      print("Kontak berhasil dihapus")


# kontak1 = {'nama': 'Joko', 'telepon': '08123456789', 'email': 'joko@gmail.com'}
# kontak2 = {'nama': 'Andi', 'telepon': '08987654321', 'email': 'andi@gmail.com'}
# kontak = [kontak1, kontak2]

kontak_kantor = Kontak()
kontak_keluarga = Kontak()

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
    break
  
  else:
    print("Anda memasukkan pilihan yang salah. Silahkan coba lagi.")
