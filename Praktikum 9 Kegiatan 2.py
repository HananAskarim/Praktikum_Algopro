b = open ("L200180170", "r")
c = b.readlines()
print c[2][:13]
print c[3][0:]+','+' '+c[1][0:10]
print c[0][:10]
b.close()
