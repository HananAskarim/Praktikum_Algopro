Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ## Kegiatan 3
>>> Nama = 'Hanan Askarim'
>>> NIM = 'L200180170'
>>> x = '1' + NIM[7:]
>>> a = int(x)
>>> b = len(Nama)
>>> type(a)
<type 'int'>
>>> type(b)
<type 'int'>
>>> a/b
90
>>> a//b
90
>>> 10*(a-999)
1710
>>> b**2
169
>>> a%b
0
>>> c = 12.5
>>> type(c)
<type 'float'>
>>> a/c
93.6
>>> a//c
93.0
>>> a%c
7.5
>>> c>b
False
>>> type(c > b)
<type 'bool'>
>>> a > b and b > c
True
>>> a > 1100 or b < 10
True
>>> 
>>> x = '1' + NIM[7:] # Variabel x menyimpan data 1 dan 3 digit NIM terakhir saya
>>> a = int(x) # variabel a menyimpan konversi string variabel x ke integer
>>> b = len(Nama) # variabel b menyimpan konversi Variabel x dengan cara menghitung jumlah huruf yang ada didalam Nama
>>> type(a) # mengecek type variabel a
<type 'int'>
>>> type(b) # mengecek type variabel b
<type 'int'>
>>> a/b # membagi varabel a dengan variabel b
90
>>> a//b # membagi variabel a dengan variabel b lalu dibulatkan menjadi puluhan
90
>>> 10*(a-999) # mengalikan 10 dengan variabel a yang dikurangi dengan 999
1710
>>> b**2 # mengkuadratkan variabel b
169
>>> a%b # menghitung hasil pembagian dari variabel a dengan b
0
>>> c = 12.5 # variabel c menyimpan angka 12.5
>>> type(c) # mengecek type variabel c
<type 'float'>
>>> a/c # membagi variabel a dengan variabel c
93.6
>>> a//c # membagi variabel a dengan variabel c lalu dibulatkan menjadi puluhan
93.0
>>> a%c # membagi hasil sisa pembagian a dengan c
7.5
>>> c>b # mengecek apakah variabel c lebih besar daripada b
False
>>> type(c > b) # menyeleksi objek type apakah variabel c lebih besar daripada b
<type 'bool'>
>>> a > b and b > c #  mengecek apakah a lebih besar b dan b lebih besar c merupakan boolean atau decision
True
>>> a > 1100 or b < 10 # mengecek a lebih besar 1100 atau b lebih kecil dari 10 merupakan boolean atau decision
True
>>> 
>>> 
>>> ## Kegiatan 4
>>> Nama = 'Hanan Askarim'
>>> NIM = 170
>>> Tinggi = 1.72
>>> Berat = 55
>>> TahunLahir = 1999
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<type 'tuple'>
>>> Aku[0]
1999
>>> a = NIM % 4; Aku[a]
1.72
>>> type(Aku[a])
<type 'float'>
>>> Aku[a:4]
(1.72, 170)
>>> type(Aku[4])
<type 'str'>
>>> Aku[0] = 'ok'

Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> type(Data)
<type 'list'>
>>> type(Data[4])
<type 'str'>
>>> Data[4][5]
' '
>>> Data[4][a:6]
'nan '
>>> Data[0] = 'ok'; Data
['ok', 55, 1.72, 170, 'Hanan Askarim']
>>> Data[-a]
170
>>> range(a)
[0, 1]
>>> 
>>> type(Aku) # Memeriksa tipe data dari Aku adalah tuple, karena ditulis dengan kurung biasa dan elemen list tidak dapat diubah
<type 'tuple'>
>>> Aku[0] # Menampilkan tahun lahir karena pada Aku indeks ke 0 adalah data dari TahunLahir
1999
>>> a = NIM % 4; Aku[a] # Karena sisa hasil bagi dari NIM = 170 dan 4 adalah 1.72 maka Aku[a] sama dengan Aku[1.72] yang menampilkan indeks ke 1.72 adalah data dari NIM
1.72
>>> type(Aku[a]) # Memeriksa tipe data dari Aku indeks ke 1.72 adalah float, 170 adalah bilangan desimal
<type 'float'>
>>> Aku[a:4] # a = 1.72 maka Aku[1.72:4] adalah menampilkan indeks 1.72 hingga indeks 4
(1.72, 170)
>>> type(Aku[4]) # Memeriksa tipe data dari Aku indeks ke 4 adalah string, karena indeks ke 4 adalah Nama menyimpan data berupa teks ‘Hanan Askarim’
<type 'str'>
>>> Aku[0] = 'ok' # Error saat indeks 0 ingin diubah dengan ‘ok’ karena elemen tuple tidak dapat diubah dan proses ini gagal

Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    Aku[0] = 'ok' # Error saat indeks 0 ingin diubah dengan ‘ok’ karena elemen tuple tidak dapat diubah dan proses ini gagal
TypeError: 'tuple' object does not support item assignment
>>> type(Data) #  Memeriksa tipe data dari Aku adalah list, karena ditulis dengan kurung siku dan elemen list dapat diubah
<type 'list'>
>>> type(Data[4]) # Memeriksa tipe data dari Data indeks ke 4 adalah string, karena indeks ke 4 adalah Nama menyimpan data berupa teks ‘Hanan Askarim’
<type 'str'>
>>> Data[4][5] # Menampilkan huruf ke 5 dari sebuah Data indeks 4
' '
>>> Data[4][a:6] # Menampilkan slicing dari indeks 3 sampai indeks 5 dari sebuah Data indeks 4
'nan '
>>> Data[0] = 'ok'; Data # Karena elemen list, indeks 0 dapat diubah menjadi string ‘ok’ dan indeks data menjadi ['ok', 55, 1.72, 170, 'Hanan Askarim']
['ok', 55, 1.72, 170, 'Hanan Askarim']
>>> Data[-a] # Menampilkan indeks 170 dari belakang maka Data[170]
170
>>> range(a) # Range untuk membuat list baru 0 – 1 karena dengan data a adalah 1.72
