#operasi yang dapat dilakukan dengan penyingkatan
#operasi ditambah dengan assignment

#aritmatika
print("\n",15*"=","ARITMATIKA",15*"=")
a = 5 #ini adalah assignment
print("nilai A adalah:",a)

a += 1 #artinya adalah a = a + 1
print("nilai A += 1, nilai a menjadi",a)

a -= 2 #artinya adalah a = a - 2
print("nilai A -= 2, nilai a menjadi",a)

a *= 5 #artinya adalah a = a * 5
print("nilai A *= 5, nilai menjadi",a)

a /= 2 #artinya adalah a = a / 2
print("nilai A /= 2, nilai a menjadi",a)

#modulus dan floor division

print("\n",15*"=","Modulus dan Floor Division",15*"=")
b = 10
print("\nNilai B adalah",b)
b %= 3 #artinya adalah b = b % 3
print("nilai b %= 3, nilai b menjadi ",b)

b = 10
b //= 3 #artinya adalah b = b // 3
print("nilai b //= 3, nilai b menjadi",b)

#pangkat atau eksponen

print("\n",15*"=","PANGKAT ATAU EKSPONEN",15*"=")
a = 5
print("\nNilai A adalah",a)
a **= 3 #artinya adalah a = a ** 3
print("nilai a **= 3, nilai a menjadi",a)

#bitwise

print("\n",15*"=","BITWISE",15*"=")
#OR
print("\nOR")
c = True
print("\nNilai C adalah",c)
c |= False #artinya adalah c = c | false
print("nilai C |= false, nilai c menjadi",c)
c |= True #artinya adalah c = c | True
print("nilai C |= True, nilai c menjadi",c)
c = False
print("\nNilai C adalah",c)
c |= True #artinya adalah c = c \ true
print("nilai C |= true, nilai c menjadi",c)
c |= False #artinya adalah c = c \ false
print("nilai C |= false, nilai c menjadi",c)
print("\nAnd")
#AND
c = True
print("\nNilai C adalah",c)
c &= False #artinya adalah C = C & false
print("nilai C &= false, nilai C menjadi",c)
c &= True #artinya adalah C = C & true
print("nilai C &= true, nilai C menjadi",c)
c = False
print("\nNilai C adalah",c)
c &= True #artinya adalah C = C & true
print("Nilai C &= true, nilai C menjadi",c)
c &= False #artinya adalah C = C & false
print("Nilai C &= false, nilai C menjadi",c)
print("\nXOR")
#XOR
c = True
print("\nNilai C adalah",c)
c ^= False #artinya adalah c = c ^ false
print("Nilai C ^= false, nilai C menjadi",c)
c ^= True #artinya adalah c = c ^ true
print("Nilai C ^= true, nilai C menjadi",c)
c = False
print("\nNilai C adalah",c)
c ^= True #artinya adalah c = c ^ true
print("Nilai C ^= true, nilai C menjadi",c)
c ^= False #artinya adalah c = c ^ false
print("Nilai C ^= false, nilai C menjadi",c)
print("\nSHIFTING")
#SHIFTING
d = 0b0100
print("\nNilai D =",format(d,'04b'))
d >>= 2 #artinya adalah d = d >> 2
print("Nilai D >>= 2, nilai D menjadi",format(d, '04b'))
d <<= 1 #artinya adalah d = d << 1
print("Nilai D <<= 1, nilai D menjadi",format(d, '04b'))
