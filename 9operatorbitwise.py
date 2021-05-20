# operator bitwise, operasi binary/biner. Bitwise = operasi masing masing bit

a = -97
b = 38
# 96 = 01100001 12 = 00100110
#bitwise OR (|) (Apabila ada true, dijadikan true)
print("\n",15*"=","OR",15*"=")
c = a | b
print("nilai a: ",a,", dengan format biner: ",format(a, '08b'))
print("nilai a: ",b,", dengan format biner: ",format(b, '08b'))
print("nilai c: ",c,", dengan format biner: ",format(c, '08b'))

#bitwise AND (&) #Akan false apabila salah satu false
print("\n",15*"=","AND",15*"=")
c = a&b
print("nilai a: ",a,", dengan format biner: ",format(a, '08b'))
print("nilai a: ",b,", dengan format biner: ",format(b, '08b'))
print("nilai c: ",c,", dengan format biner: ",format(c, '08b'))

#bitwise XOR (^) #Akan menjadi false apabila dua duanya true, tetap false apabila kedua false
print("\n",15*"=","XOR",15*"=") 
c = a^b
print("nilai a: ",a,", dengan format biner: ",format(a, '08b'))
print("nilai a: ",b,", dengan format biner: ",format(b, '08b'))
print("nilai c: ",c,", dengan format biner: ",format(c, '08b'))

#bitwise NOT (~) #Di balik sifat nya dari + menjadi - dan diawali dari -1 bukan 0
print("\n",15*"=","NOT",15*"=") 
c = ~a
print("nilai a: ",a,", dengan format biner: ",format(a, '08b'))
print("nilai a: ",b,", dengan format biner: ",format(b, '08b'))
print("nilai c: ",c,", dengan format biner: ",format(c, '08b'))

#shifting

#shift right(>>)
print("\n",15*"=","SHIFTING RIGHT",15*"=")
d = a >> 1

print("nilai a: ",a,", dengan format biner: ",format(a, '08b'))
print("nilai d: ",d,", dengan format biner: ",format(d, '08b'))

#shift left(<<)
print("\n",15*"=","SHIFTING LEFT",15*"=")
d = a << 2

print("nilai a: ",a,", dengan format biner: ",format(a, '08b'))
print("nilai d: ",d,", dengan format biner: ",format(d, '08b'))
