DaftarKaryawan = [
    {
        'NIK' : 513001,
        'Nama' : 'Usain Bolt',
        'Jenis Kelamin' : 'Laki-laki',
        'Tanggal Lahir' : '21/08/1986',
        'Jabatan' : 'Supervisor'
    },
    {
        'NIK' : 513002,
        'Nama' : 'Serena Williams',
        'Jenis Kelamin' : 'Perempuan',
        'Tanggal Lahir' : '26/09/1981',
        'Jabatan' : 'Supervisor'
    },
      {
        'NIK' : 513003,
        'Nama' : 'Marc Guiu',
        'Jenis Kelamin' : 'Laki-laki',
        'Tanggal Lahir' : '04/01/2006',
        'Jabatan' : 'Staff'
    },
        {
        'NIK' : 513004,
        'Nama' : 'Putri Kusuma',
        'Jenis Kelamin' : 'Perempuan',
        'Tanggal Lahir' : '20/07/2002',
        'Jabatan' : 'Staff'
    },
        {
        'NIK' : 513005,
        'Nama' : 'Chris Bumstead',
        'Jenis Kelamin' : 'Laki-laki',
        'Tanggal Lahir' : '02/02/1995',
        'Jabatan' : 'Supervisor'
    },
        {
        'NIK' : 513006,
        'Nama' : 'Nozomi Okuhara',
        'Jenis Kelamin' : 'Perempuan',
        'Tanggal Lahir' : '13/03/1995',
        'Jabatan' : 'Staff'
    },
        {
        'NIK' : 513007,
        'Nama' : 'Cristiano Ronaldo',
        'Jenis Kelamin' : 'Laki-laki',
        'Tanggal Lahir' : '05/02/1985',
        'Jabatan' : 'Manager'
    }
]

def InputNIK() :
    while(True) :
        i = 0
        NIKpegawai = int(input('\nMasukkan NIK : '))
        for x in range(len(DaftarKaryawan)) :
            if(NIKpegawai == DaftarKaryawan[x]['NIK']) :
                i = 1
        if(i == 1) :
            print('NIK sudah terdaftar. Coba masukkan yang lain!')
        else :
            return NIKpegawai

def FormatTanggal1(x) :
    while(True) :
        text1 = 'Masukkan tanggal lahir (DD/MM/YYYY) : '
        text2 = 'Edit tanggal lahir (DD/MM/YYYY) : '
        if(x == 2) :
            tanggalLahir = input(text1)
        elif(x == 4) :
            tanggalLahir = input(text2)
        slash1 = tanggalLahir[2:3]
        slash2 = tanggalLahir[5:6]
        if(len(tanggalLahir) < 10 or len(tanggalLahir) > 10) :
            print('=== Format tanggal salah. Mohon masukkan tanggal sesuai dengan panjang format yang benar (DD/MM/YYYY). ===')
        elif(slash1 != '/' or slash2 != '/') :
            print('=== Format tanggal salah. Mohon masukkan tanggal sesuai dengan format berikut (DD/MM/YYYY). ===')
        else :
            return tanggalLahir
 
def FormatTanggal(tipe) :
    while(True) :
        if(tipe == 2) :
            tanggal_Lahir = FormatTanggal1(2)
        elif(tipe == 4) :
            tanggal_Lahir = FormatTanggal1(4)
        hari = int(tanggal_Lahir[:2])
        bulan = int(tanggal_Lahir[3:5])
        tahun = int(tanggal_Lahir[6:])
        if(hari > 31) :
            print('=== Input Hari (DD) salah. Mohon masukkan sesuai dengan format tanggal yang benar! ===')
        elif(bulan > 12) :
            print('=== Input Bulan (MM) salah. Mohon masukkan sesuai dengan format tanggal yang benar! ===')
        elif(tahun < 1900) :
            print('=== Input Tahun (YYYY) salah. Mohon masukkan sesuai dengan format tanggal yang benar! ===')
        else :
            return tanggal_Lahir

def Jenis_Kelamin(tipe) :
    while(True) :
        text1 = 'Masukkan jenis kelamin : '
        text2 = 'Edit jenis kelamin : '
        if(tipe == 2) :
            JenisKelamin = input(text1)
        elif(tipe == 4) :
            JenisKelamin = input(text2)

        if(JenisKelamin == 'Laki-laki') :
            break
        elif(JenisKelamin == 'Perempuan') :
            break
        else :
            print("=== Input salah, untuk jenis kelamin mohon masukkan 'Laki-laki' atau 'Perempuan'! ===")

def konfirmasiKeluar() :
    while(True) :
        konfirmasi = input('\nTekan 0 untuk kembali ke Menu sebelumnya : ')
        if(konfirmasi == '0') :
            break
        else :
            print("\n=== Input salah. Mohon masukkan nomor sesuai dengan instruksi! ===")

def titik():
    dots = ''
    for i in range(130) :
        dots += '.'
    print(dots)

def filterNIK(tipe) :
    text1 = '\nMasukkan NIK Karyawan yang dituju: '
    text2 = '\nMasukkan pencarian NIK Karyawan : '
    if(tipe == 1) :
        inputNIK = int(input(text1))
        print('\n<< Data Karyawan dengan NIK : {} di PT. Sehat Bersama>>\n'.format(inputNIK))
    elif(tipe == 2) :
        MenampilkanDaftarKaryawan(0)
        inputNIK = int(input(text2))
        print('\n<< Hasil Filter >>\n')
    filter_NIK = filter(lambda x : x['NIK'] == inputNIK, DaftarKaryawan)
    titik()   
    for y in filter_NIK :
      nomor = (DaftarKaryawan.index(y) + 1)
      print('{}. NIK : {}, Nama Karyawan : {}, Jenis Kelamin : {}, Tanggal Lahir : {}, Jabatan : {}'.format(nomor, y['NIK'], y['Nama'], y['Jenis Kelamin'], y['Tanggal Lahir'], y['Jabatan']))
    titik()
    konfirmasiKeluar()

def filterNama() :
    MenampilkanDaftarKaryawan(0)
    inputNama = input('\nMasukkan pencarian Nama Karyawan : ')
    filter_nama = filter(lambda x : x['Nama'].__contains__(inputNama) or (x['Nama'].lower()).__contains__(inputNama), DaftarKaryawan)
    print('\n<< Hasil Filter >>\n')
    titik()   
    for y in filter_nama :
      nomor = (DaftarKaryawan.index(y) + 1)
      print('{}. NIK : {}, Nama Karyawan : {}, Jenis Kelamin : {}, Tanggal Lahir : {}, Jabatan : {}'.format(nomor, y['NIK'], y['Nama'], y['Jenis Kelamin'], y['Tanggal Lahir'], y['Jabatan']))
    titik()
    konfirmasiKeluar()

def filterJeniskelamin() :
    MenampilkanDaftarKaryawan(0)
    inputJeniskelamin = input('\nMasukkan pencarian Jenis Kelamin Karyawan : ')
    filter_Jeniskelamin = filter(lambda x : x['Jenis Kelamin'].__contains__(inputJeniskelamin) or (x['Jenis Kelamin'].lower()).__contains__(inputJeniskelamin), DaftarKaryawan)
    print('\n<< Hasil Filter >>\n')
    titik()   
    for y in filter_Jeniskelamin :
      nomor = (DaftarKaryawan.index(y) + 1)
      print('{}. NIK : {}, Nama Karyawan : {}, Jenis Kelamin : {}, Tanggal Lahir : {}, Jabatan : {}'.format(nomor, y['NIK'], y['Nama'], y['Jenis Kelamin'], y['Tanggal Lahir'], y['Jabatan']))
    titik()
    konfirmasiKeluar()

def filterTanggallahir() :
    MenampilkanDaftarKaryawan(0)
    print('''
Format pencarian Hari pada Tanggal Lahir, ketik 'DD/' (contoh : '05/')
Format pencarian Bulan pada Tanggal Lahir, ketik '/MM/' (contoh : '/02/')
Format pencarian Tahun pada Tanggal Lahir, ketik '/YYYY' (contoh : '/1995')
Format pencarian Tanggal Lahir secara keseluruhan, ketik 'DD/MM/YYYY' (contoh : '02/02/1995')''')
    inputTanggalahir = input('\nMasukkan pencarian Tanggal Lahir Karyawan : ')
    filter_Tanggallahir = filter(lambda x : x['Tanggal Lahir'].__contains__(inputTanggalahir), DaftarKaryawan)
    print('\n<< Hasil Filter >>\n')
    titik()   
    for y in filter_Tanggallahir :
      nomor = (DaftarKaryawan.index(y) + 1)
      print('{}. NIK : {}, Nama Karyawan : {}, Jenis Kelamin : {}, Tanggal Lahir : {}, Jabatan : {}'.format(nomor, y['NIK'], y['Nama'], y['Jenis Kelamin'], y['Tanggal Lahir'], y['Jabatan']))
    titik()
    konfirmasiKeluar()

def filterJabatan() :
    MenampilkanDaftarKaryawan(0)
    inputJabatan = input('\nMasukkan pencarian Jabatan Karyawan : ')
    filter_Jabatan = filter(lambda x : x['Jabatan'].__contains__(inputJabatan) or (x['Jabatan'].lower()).__contains__(inputJabatan), DaftarKaryawan)
    print('\n<< Hasil Filter >>\n')
    titik()   
    for y in filter_Jabatan :
      nomor = (DaftarKaryawan.index(y) + 1)
      print('{}. NIK : {}, Nama Karyawan : {}, Jenis Kelamin : {}, Tanggal Lahir : {}, Jabatan : {}'.format(nomor, y['NIK'], y['Nama'], y['Jenis Kelamin'], y['Tanggal Lahir'], y['Jabatan']))
    titik()
    konfirmasiKeluar()

def MenuFilterDaftarKaryawan() :
    while True :
        menu = (input(''' 
<< Menu Filter Daftar Karyawan >>

List Menu:
1. Filter NIK Karyawan
2. Filter Nama Karyawan
3. Filter Jenis Kelamin Karyawan
4. Filter Tanggal Lahir Karyawan
5. Filter Jabatan Karyawan
                 
0. Kembali ke Menu Utama                                                    
                                        
Masukkan angka menu yang ingin dijalankan : '''))
        if (menu == '1') :
            filterNIK(2)
        elif(menu == '2') :
            filterNama()
        elif(menu == '3') :
            filterJeniskelamin()
        elif(menu == '4') :
            filterTanggallahir()
        elif(menu == '5') :
            filterJabatan()
        elif(menu == '0') :
           break
        else :
            print('\n=== Input salah. Mohon masukkan nomor sesuai dengan pilihan menu yang tertera! ===')

def MenampilkanDaftarKaryawan(confirm) :
    print('\n<< Daftar Karyawan PT. Sehat Bersama >>\n')
    titik()
    for x in range(len(DaftarKaryawan)) :
        print('{}. NIK : {}, Nama Karyawan : {}, Jenis Kelamin : {}, Tanggal Lahir : {}, Jabatan : {}'.format(
            x+1, DaftarKaryawan[x]['NIK'], DaftarKaryawan[x]['Nama'], DaftarKaryawan[x]['Jenis Kelamin'], DaftarKaryawan[x]['Tanggal Lahir'],DaftarKaryawan[x]['Jabatan']
        ))
    titik()
    if(confirm == 1) :
        konfirmasiKeluar()
    elif(confirm == 0) :
        print('')

def MemunculkanDaftarKaryawan() :
    while True :
        menu = (input(''' 
<< Menu Tampilan Daftar Karyawan >>

List Menu:
1. Menampilkan seluruh Daftar Karyawan
2. Menampilkan sebagian Daftar Karyawan
                 
0. Kembali ke Menu Utama                                                    
                                        
Masukkan angka menu yang ingin dijalankan : '''))
        if (menu == '1') :
            MenampilkanDaftarKaryawan(1)
        elif(menu == '2') :
            filterNIK(1)
        elif(menu == '0') :
           break
        else :
            print('\n=== Input salah. Mohon masukkan nomor sesuai dengan pilihan menu yang tertera! ===')

def MenambahkanDaftarKaryawan() :
    print('\n<< Menambahkan Daftar Karyawan PT. Sehat Bersama >>')
    while(True) :
        NIKkaryawan = InputNIK()
        if(NIKkaryawan < 513000) :
            print("=== Input salah. Mohon masukkan nilai NIK paling sedikit 6 huruf dengan format '513xxx'. ===")
        else :
            break
    NamaKaryawan = input('Masukkan nama karyawan : ')
    JenisKelamin = Jenis_Kelamin(2)
    TanggalLahir = FormatTanggal(2)
    Jabatan = input('Masukkan jabatan karyawan : ')
    while(True) :
        konfirmasi = input('\nApakah Anda yakin akan menyimpan data di atas? (ya/tidak): ')
        if(konfirmasi == 'Ya' or konfirmasi == 'ya') :
            DaftarKaryawan.append({
                'NIK' : NIKkaryawan,
                'Nama' : NamaKaryawan,
                'Jenis Kelamin' : JenisKelamin,
                'Tanggal Lahir' : TanggalLahir,
                'Jabatan' : Jabatan})
            MenampilkanDaftarKaryawan(0)
            print('Data berhasil ditambahkan.')
            break
        elif(konfirmasi == 'Tidak' or konfirmasi == 'tidak') :
            print('\nData tidak berhasil ditambahkan. Silakan akses kembali menu ini jika hendak menambahkan data baru.')
            break
        else :
            print("\n=== Input salah. Mohon masukkan 'ya' atau tidak' ===")

def MenghapusDaftarKaryawan() :
    MenampilkanDaftarKaryawan(0)
    while(True) :
        IndexKaryawan = int(input('Masukkan nomor pada daftar karyawan yang ingin dihapus : '))
        if(IndexKaryawan <= 0 or IndexKaryawan > len(DaftarKaryawan)) :
            print('=== Input salah. Mohon masukkan nomor sesuai dengan daftar karyawan yang ada di atas! ===')
        else :
            break   
    while(True) :
        konfirmasi = input('\nApakah Anda yakin akan menghapus data di atas? (ya/tidak): ')
        if(konfirmasi == 'Ya' or konfirmasi == 'ya') :
            del DaftarKaryawan[IndexKaryawan-1]
            MenampilkanDaftarKaryawan(0)
            print('Data berhasil terhapus.')
            break
        elif(konfirmasi == 'Tidak' or konfirmasi == 'tidak') :
            print('\nData tidak berhasil terhapus. Silakan akses kembali menu ini jika hendak menghapus data yang diinginkan.')
            break
        else :
            print("\n=== Input salah. Mohon masukkan 'ya' atau tidak' ===")

def MengeditDaftarKaryawan() :
    MenampilkanDaftarKaryawan(0)
    while(True) :
        x = int(input('Masukkan nomor pada daftar karyawan yang ingin diedit : '))
        if(x <= 0 or x > len(DaftarKaryawan)) :
            print('=== Input salah. Mohon masukkan nomor sesuai dengan daftar karyawan yang ada di atas! ===')
        else :
            y = x-1
            print('\nNIK : {}, Nama Karyawan : {}, Jenis Kelamin : {}, Tanggal Lahir : {}, Jabatan : {}\n'.format(DaftarKaryawan[y]['NIK'], DaftarKaryawan[y]['Nama'], DaftarKaryawan[y]['Jenis Kelamin'], DaftarKaryawan[y]['Tanggal Lahir'],DaftarKaryawan[y]['Jabatan']))
            break
    NamaKaryawan = input('Edit nama karyawan : ')
    JenisKelamin = Jenis_Kelamin(4)
    TanggalLahir = FormatTanggal(4)
    Jabatan = input('Edit jabatan karyawan : ')
    while(True) :
        konfirmasi = input('\nApakah Anda yakin akan menyimpan perubahan data di atas? (ya/tidak): ')
        if(konfirmasi == 'Ya' or konfirmasi == 'ya') :
            DaftarKaryawan[x-1].update({
                'Nama' : NamaKaryawan,
                'Jenis Kelamin' : JenisKelamin,
                'Tanggal Lahir' : TanggalLahir,
                'Jabatan' : Jabatan})
            MenampilkanDaftarKaryawan(0)
            print('Data berhasil diedit.')
            break
        elif(konfirmasi == 'Tidak' or konfirmasi == 'tidak') :
            print('\nData tidak tersimpan. Silakan akses kembali menu ini jika hendak mengedit data baru.')
            break
        else :
            print("\n=== Input salah. Mohon masukkan 'ya' atau tidak' ===")

while(True):
    PilihanMenu = input('''
--------------------------------------------                        
 Data Karyawan Perusahaan PT. Sehat Bersama 
--------------------------------------------
       
List Menu:
1. Menampilkan Daftar Karyawan
2. Menambah Daftar Karyawan
3. Menghapus Daftar Karyawan
4. Mengedit Daftar Karyawan
5. Filter Daftar Karyawan
6. Keluar/Exit Menu
                                        
Masukkan angka menu yang ingin dijalankan : ''')
    
    if(PilihanMenu == '1') :
        MemunculkanDaftarKaryawan()
    elif(PilihanMenu == '2') :
        MenambahkanDaftarKaryawan()
    elif(PilihanMenu == '3') :
        MenghapusDaftarKaryawan()
    elif(PilihanMenu == '4') :
        MengeditDaftarKaryawan()
    elif(PilihanMenu == '5') :
        MenuFilterDaftarKaryawan()
    elif(PilihanMenu == '6') :
        break
    else :
        print('\n=== Input salah. Mohon masukkan nomor sesuai dengan pilihan menu yang tertera! ===')
