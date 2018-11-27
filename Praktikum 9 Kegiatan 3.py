import shelve
a = open('L200180170', 'r')
NIM = a.readline()
TL = a.readline()
Nama = a.readline()
a.close()

a = shelve.open('Hanan')
a['b'] = [NIM, TL, Nama]
a.close()
