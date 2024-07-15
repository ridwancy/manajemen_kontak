'Berisi fungsi membuka dan menyimpan kontak'

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