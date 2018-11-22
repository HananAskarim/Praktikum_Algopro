x={'NIM':'L200180170','Nama':'Hanan Askarim','Alamat':'Sragentina','Kodepos':'57292','Tanggal lahir':'12 Juli 1999','Tinggi badan':'174','Berat badan':'60'}
b="""Pilihan yang tersedia:
b menampilkan bantuan ini
N menampilkan NIM
n menampilkan Nama
A menampilkan Alamat
K menampilkan kodepos
T menampilkan Tanggal lahir
t menampilkan Tinggi badan
B menampilkan Berat badan
k keluar\n"""
def nim():
    print 'NIM: '+x['NIM']
def nama():
    print 'Nama: '+x['Nama']
def alamat():
    print 'Alamat: '+x['Alamat']
def kodepos():
    print 'Kodepos: '+x['Kodepos']
def tanggallahir():
    print 'Tanggal lahir: '+x['Tanggal lahir']
def tbadan():
    print 'Tinggi badan: '+x['Tinggi badan']
def beratbadan():
    print 'Berat badan: '+x['Berat badan']
key = ('b', 'N', 'n', 'A', 'K', 'T', 't', 'B', 'k')
print b
data = raw_input("Pilihan saudara: ")
while data != 'k':
    if data == 'b':
        print b
        data = raw_input("Pilihan saudara: ")
    elif data == 'N':
        nim ()
        data = raw_input("Pilihan saudara: ")
    elif data == 'n':
        nama ()
        data = raw_input("Pilihan saudara: ")
    elif data == 'A':
        alamat ()
        data = raw_input("Pilihan saudara: ")
    elif data == 'K':
        kodepos ()
        data = raw_input("Pilihan saudara: ")
    elif data == 'T':
        tlahir ()
        data = raw_input("Pilihan saudara: ")
    elif data == 't':
        tbadan ()
        data = raw_input("Pilihan saudara: ")
    elif data == 'B':
        bbadan ()
        data = raw_input("Pilihan saudara: ")
    elif data != key:
        print "perintah tidak dikenal"
        data = raw_input("Pilihan saudara: ")
else:
        print "Terima Kasih"
    
        
