import sys 
import pyinputplus as pypi

listBuku = [
    ['P11', 'Python Programming', 'John Smith', 'pemrograman', '5'],
    ['DS12', 'Data Science Handbook', 'Jane Doe', 'Data Science', '9'],
    ['PD13', 'Atomic Habits', 'James Clear', 'Pengembangan Diri', '4'],
    ['P14', 'Naruto', 'Masashi Kishimoto', 'Komik', '12'],
    ['D15', 'Dilan 1990', 'Pidi Baiq', 'Novel', '6'],
]

#Main Menu
def fiturRead():
    sub_menu = 0
    while (True):
        print('''
        ----- Menampilkan Data Buku -----

        1. Tampilkan Daftar Buku yang Tersedia
        2. Cari Dengan ID Buku
        3. Kembali ke Menu Utama
        -----------------------------------------
    ''')
        sub_menu = int(input("Pilih Menu Tampilan Data: "))

        if sub_menu == 1:
            print("Daftar Buku:")
            for row in listBuku:
                print("ID : {}, judul : {}, penulis : {}, kategori : {}, stok : {}".format(row[0],row[1],row[2],row[3],row[4]))
        elif sub_menu == 2:
            id = input("Masukkan ID: ")
            exists = False
            data = []

            for row in listBuku:
                if row[0] == id:
                    exists = True
                    data = row

            if exists:
                print("Data Buku dengan ID: {}".format(id))
                print("ID : {}, judul : {}, penulis : {}, kategori : {}, stok : {}".format(data[0],data[1],data[2],data[3],data[4]))
            else:
                print("-----Tidak Ada Data Buku-----")
        elif sub_menu == 3:
            break
        else:
            pass
        print()


#Create Menu
def fiturCreate ():
    sub_menu = 0
    while (True):
        print('''
            ----- Menambahkan Data Buku -----

            1. Tambah Data Buku
            2. Kembali ke Menu Utama
            ---------------------------------- 
        ''')
        sub_menu = int(input("Pilih Menu Menambahkn Data: "))
                   
        if sub_menu == 1:
            id = input("Maukkan ID Buku :")
            exists = False
            for row in listBuku:
                if row[0] == id:
                    exists = True

            if exists:
                    print("Data sudah tersedia")
            else:
                judulBuku = input("Masukkan Judul Buku :")
                penulis = input("Masukkan Nama Penulis :")
                kategoriBuku = input("Masukkan Kategori Buku :")
                jumlahstok = input("Masukkan Jumlah Stok :")
                    
                while(True):
                    pertanyaan = input('Apakah Data Buku Akan Disimpan? (ya/tidak) :')

                    if (pertanyaan == 'ya'):
                        row = [id, judulBuku, penulis, kategoriBuku, jumlahstok]
                        listBuku.append(row)
                        print('Data Buku Berhasil Ditambah')
                        break
                    if(pertanyaan == 'tidak'):
                        break
                    print()

        elif sub_menu == 2:
            break
        else:
            pass

#Update Menu
def fiturUpdate ():
    sub_menu = 0
    while (True):
        print('''
            ----- Mengubah Data Buku -----

            1. Update Data Buku
            2. Kembali ke Menu Utama
        ''')
        sub_menu = int(input("Pilih Menu Update Data: "))
        if sub_menu == 1:
            id = input("Masukkan ID :")
            exists = False
            index = 0

            i = 0
            for row in listBuku:
                if row[0] == id:
                    exists = True
                    index = i
                    break
                i = i + 1

            if exists:
                data = listBuku[index]
                print("ID : {}, judul : {}, penulis : {}, kategori : {}, stok : {}".format(data[0],data[1],data[2],data[3],data[4]))
                while(True):
                    pertanyaan = input("Ketik Y jika ingin update atau N Jika Ingin Cancel Update (Y/N) :")
                    if pertanyaan == "Y":
                        kolom = input("Masukkan Kolom yang Ingin di Edit\n(Judul/Penulis/Kategori/Stok):")

                        if kolom == "Judul":
                            judulBaru = input("Masukkan Judul Buku baru:")
                            while (True):
                                pertanyaan2 = input("Apakah Data Akan di Update (Y/N): ")
                                if pertanyaan2 == "Y":
                                    listBuku[index][1] = judulBaru
                                    print("Data Update")
                                    break
                                elif pertanyaan2 == "N":
                                    print("Data Tidak Terupdate")
                                    break
                                else:
                                    pass
                        if kolom == "Penulis":
                            penulisBaru = input("Masukkan Penulis Buku baru:")
                            while (True):
                                pertanyaan2 = input("Apakah Data Akan di Update (Y/N): ")
                                if pertanyaan2 == "Y":
                                    listBuku[index][2] = penulisBaru
                                    print("Data Update")
                                    break
                                elif pertanyaan2 == "N":
                                    print("Data Tidak Terupdate")
                                    break
                                else:
                                    pass
                        if kolom == "Kategori":
                            kategoriBaru = input("Masukkan Kategori Buku baru:")
                            while (True):
                                pertanyaan2 = input("Apakah Data Akan di Update (Y/N): ")
                                if pertanyaan2 == "Y":
                                    listBuku[index][3] = kategoriBaru
                                    print("Data Update")
                                    break
                                elif pertanyaan2 == "N":
                                    print("Data Tidak Terupdate")
                                    break
                                else:
                                    pass
                        elif kolom == "Stok":
                            stokBaru = input("Masukkan Stok Buku baru:")
                            while (True):
                                pertanyaan2 = input("Apakah Data Akan di Update (Y/N): ")
                                if pertanyaan2 == "Y":
                                    listBuku[index][4] = stokBaru
                                    print("Data Update")
                                    break
                                elif pertanyaan2 == "N":
                                    print("Data Tidak Terupdate")
                                    break
                                else:
                                    pass

                        break
                    if pertanyaan == "N":
                        print("Data Tidak Terhapus")
                        break
                print()
            else:
                print("Data Tidak Ada")
                print()
        elif sub_menu == 2:
            break
        else:
            pass

#Delete Menu
def fiturDelete ():
    sub_menu = 0
    while (True):
        print('''
            ----- Menghapus Data Buku -----

            1. Menghapus Data Buku
            2. Kembali ke Menu Utama
            --------------------------------
        ''')
        sub_menu = int(input("Pilih Menu Update Data: "))

        if sub_menu == 1:
            id = input("Masukkan ID :")
            exists = False
            index = 0

            i = 0
            for row in listBuku:
                if row[0] == id:
                    exists = True
                    index = i
                    break
                i = i + 1

            if exists:
                while(True):
                    pertanyaan = input("Apakah Data Akan di Hapus? (Y/N):")

                    if pertanyaan == "Y":
                        listBuku.pop(index)
                        print("Data Delete")
                        break
                    if pertanyaan == "N":
                        print("Data Tidak Terhapus")
                        break
                print()
            else:
                print("Data Tidak Ada")
                print()
        elif sub_menu == 2:
            break
        else:
            pass

#Function
main_menu = 0

def show_menu():
    print('''
            ----- stok peminjaman perpustakaan -----

            1. Fitur Read 
            2. Fitur Create 
            3. Fitur Update 
            4. Fitur Delete 
            5. Exit Program
            -----------------------------------------
    ''')
while (True):
    show_menu()
    main_menu = int(input("Pilih Menu Utama: "))
    print()
    
    if main_menu ==  1:
        fiturRead()
    elif main_menu == 2:
        fiturCreate()
    elif main_menu == 3:
        fiturUpdate()
    elif main_menu == 4:
        fiturDelete()
    elif main_menu == 5:
        print('\nTerimakasih Sudah Berkunjung \nDitunggu Kedatangannya Kembali\n')
        break
    else:
        print("Menu yang anda pilih tidak tersedia. Silahkan coba lagi.")
    print()








                    







