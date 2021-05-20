# operasi dan manipulasi string

#1. Menyambung string (concatenate)
nama_pertama = "Rahmadiyan"
nama_tengah = ""
nama_akhir = "Muhammad"

print("\n")
nama_lengkap = nama_pertama + nama_tengah +" "+ nama_akhir
print("Nama lengkap ucup: ",nama_lengkap)

#2. Menghitung panjang string
panjang = len(nama_lengkap)
print("Panjang dari ",nama_lengkap,":",str(panjang))
print("\n")

#3. Operator untuk string

# mengecek apakah ada komponen char atau string di dalam string

cek_komponen = "D"
status = cek_komponen in nama_lengkap
print("Komponen " + cek_komponen + " ada di " + nama_lengkap +": "+ str(status))
print("\n")

#mengecek apakah tidak ada komponen char atau string di dalam string

cek_komponen = "d"
status = cek_komponen not in nama_lengkap
print("Komponen " + cek_komponen + " tidak ada di " + nama_lengkap +": "+ str(status))
print("\n")

#mengulang string

print(15*"wk")
print("\n")

#indexing

print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[1])
print("index ke-2 : " + nama_lengkap[2])
print("index ke-3 : " + nama_lengkap[3])
print("index ke-4 : " + nama_lengkap[4])
print("index ke-5 : " + nama_lengkap[5])
print("index ke-6 : " + nama_lengkap[6])
print("index ke-7 : " + nama_lengkap[7])
print("index ke-8 : " + nama_lengkap[8])
print("index ke-9 : " + nama_lengkap[9])
print("index ke-10 : " + nama_lengkap[10])
print("index ke-(-11) :" + nama_lengkap[-11])
print("\n")

#range idexing menggunakan (:) contoh index 1 - 4 = 1:4

print("index ke-[0:4] : " + nama_lengkap[0:4])
print("index ke-[5:11] : " + nama_lengkap[5:12])
print("index ke-[0,2,4,6,8,10] : " +nama_lengkap[0:10:2])
print("\n")

#indentifying unit paling kecil dalam ASCII code

print("paling kecil: ", min(nama_lengkap))
print("\n")

#identifying unit paling besar dalam ASCII code

print("paling besar: ",max(nama_lengkap))
print("\n")

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah: ", str(ascii_code))
data = 117
print("data untuk ASCII code ",data,"adalah: ", chr(data))
print("\n")

#operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada data ",data,"adalah: ", str(jumlah))