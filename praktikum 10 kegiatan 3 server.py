import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50005))
s.listen(5)
print "Server sudah siap"
perintah = ''
p=0
l=0
t=0
while perintah != 'keluar':
    komm, addr = s.accept()
    while perintah != 'keluar':
        data = komm.recv(1024).lower().split("=")
        perintah = data[0]
        if perintah == 'keluar':
            s.close()
            break
        print 'Pesan:', perintah
        if len(data) == 2:
            if perintah == 'panjang':
                p = int(data[1])
                respon = "panjang dicatat"
                komm.send(respon)
            elif perintah == 'lebar':
                l = int(data[1])
                respon = "lebar dicatat"
                komm.send(respon)
            elif perintah == 'tinggi':
                t = int(data[1])
                respon = "tinggi dicatat"
                komm.send(respon)
            else:
                komm.send('pesan tidak diketahui')
        elif perintah == 'hitung':
            L = int((p*l+p*t+l*t)*2)
            respon = "Luas balok dengan panjang: {}, lebar: {}, dan tinggi: {} adalah {}".format(p,l,t,L)
            komm.send(respon)
        else:
            komm.send('pesan tidak diketahui')
