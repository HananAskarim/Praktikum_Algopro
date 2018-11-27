import shelve
a = shelve.open('Hanan')
print 'NIM   :',a['b'][0]
print 'TL    :',a['b'][1]
print 'Nama  :',a['b'][2]
a.close()
