"Program Manajemen Kontak"

kontak1 = {'nama': 'Joko', 'telepon': '08123456789', 'email': 'joko@gmail.com'}
kontak2 = {'nama': 'Andi', 'telepon': '08987654321', 'email': 'andi@gmail.com'}
kontak = [kontak1, kontak2]

while True:
  print("\nMenu Kontak")
  print("1. Daftar Kontak")
  print("2. Tambah Kontak")
  print("3. Menghapus Kontak")
  print("4. Keluar")

  pilihan = input("Pilih menu: ")

  if pilihan == "1":
    print("\nDaftar Kontak")
    if kontak:
      for num, item in enumerate(kontak, start=1):
        print(f'{num}. {item["nama"]} ({item["telepon"]}, {item["email"]})')
    else:
      print("Kontak kosong")
  
  elif pilihan == "2":
    print("Tambah Kontak")
    nama = input("Masukkan nama kontak baru: ")
    telepon = input("Masukkan nomor telepon kontak baru: ")
    email = input("Masukkan email kontak baru: ")
    kontak_baru = {'nama': nama, 'telepon': telepon, 'email': email}
    kontak.append(kontak_baru)
    print("Kontak berhasil ditambahkan")
    
  elif pilihan == "3":
    if kontak:
      for num, item in enumerate(kontak, start=1):
        print(f'{num}. {item["nama"]} ({item["telepon"]}, {item["email"]})')
    else:
      print("Kontak kosong")
      continue
      
    i_hapus = input("Pilih nomor kontak yang akan dihapus: ")
    del kontak[int(i_hapus)-1]
    print("Kontak berhasil dihapus")
    
  elif pilihan == "4":
    break
  
  else:
    print("Anda memasukkan pilihan yang salah. Silahkan coba lagi.")
