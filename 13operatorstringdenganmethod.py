#operator dalam bentuk methods

#merubah case(Upper dan Lower) dari string

#merubah semua ke UpperCase

salam = "Bro!"
print("Normal = ",salam)
salam = salam.upper()
print("Diubah semua ke UpperCase menjadi :",salam)
print("\n")

#merubah semua ke LowerCase

alay = "aKu KecE aBieZZzzZ"
print("Normal: ",alay)
alay = alay.lower()
print("Diubah menjadi LowerCase: ",alay)
print("\n")

#pengencekan dengan methode isX

#contoh untuk pengencekan lowercase
salam = "sist"
apakahLower = salam.islower()
print(salam + " is lower: "+ str(apakahLower))
apakahUpper = salam.isupper()
print(salam + " is Upper: " + str(apakahUpper))
print("\n")

#isalpha() --> untuk mengecek apakah semuanya huruf

nama = "rahmadiyan muhammad" #false karena terdapat spasi
isalpha = nama.isalpha()
print(nama + " is Alpha: " + str(isalpha))
print("\n")

#isalnum() --> untuk mengecek apakah semuanya huruf dan angka, bisa untuk ngecek password

password = "rahmadiyan69"
isalnum = password.isalnum()
print(password + "i s alnum: " + str(isalnum))
print("\n")

#isdecimal() --> untuk mengecek apakah semuanya angka

tahunlahir = "1999"
isdecimal = tahunlahir.isdecimal()
print(tahunlahir + " is decimal: " + str(isdecimal))
print("\n")

#isspace() --> untuk mengecek apakah hanya terisi spasi, tab, newline \n

kalimat = "\n" 
isspace = kalimat.isspace()
print(kalimat + " is Space: " + str(isspace))
print("\n")

#istitle() --> untuk mengecek apakah semua kata dimulai dengan huruf depan

judul = "It Is Okay Not To Be Orkay"
cekjudul = judul.istitle()
print(judul + " is Title: " + str(cekjudul))
print("\n")

#ngecek komponen dengan startswith() endswith() <<-- keren
cekstart = "Rahmadiyan Muhammad".startswith("rahmadiyan") #harus case sensitive
print("Start with: " + str(cekstart))
cekends = "Rahmadiyan Muhammad".endswith("Muhammad") #harus case sensitive
print("Cek end: " + str(cekends))
print("\n")

#penggabungan komponen join() dan split()
pisah = ['aku','sayang','kamu']
gabung = ' '.join(pisah)
print("gabungan dari: ",pisah," adalah: ",gabung)

gabungan = "aku sayang kamu"
print("split dari ",gabungan," adalah: ",gabungan.split(' '))
print("\n")

#alokasi karakter rjust(), ljust(), center()
contohdata = """5*"=","DATA","="*5""" #menghasilkan =====DATA===== pada terminal. RIBET

kanan = "kanan".rjust(40,"=")
print("'",kanan,"'")

kiri = "kiri".ljust(40,"=")
print("'",kiri,"'")

tengah = "tengah".center(40,"=")
print("'",tengah,"'")
print("\n")

#kebalikan alokasi karakter dengan strip()
tengah = tengah.strip("=") #menghilangkan tanda "="
print("'",tengah,"'")