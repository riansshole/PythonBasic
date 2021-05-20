# format string

# contoh generik
## perkenalan
print("\n")
nama = "Rahmadiyan Muhammad"
umur = 22 #ditambah dengan :d pada {umur:d} agar terminal membaca itu angka bulat
kuliah = "Universitas Indonesia"
tanggallahir = 29
bulanlahir = "Januari"
tahunlahir = 1999
tempatlahir = "Jakarta"
kegiatan = "mengikuti kelas QA Cilsy"
muridcilsy = True
suhutempattinggal = 27.6
biaya = 1850000

format_str = f"Hello, nama saya adalah {nama}, saya tinggal di tempat dengan suhu {suhutempattinggal}.\nSaya berumur {umur:d}, saya lahir di {tempatlahir} pada {tanggallahir} {bulanlahir} {tahunlahir}.\nSaya berkuliah di {kuliah}.\nKesibukan saya sekarang adalah {kegiatan}\nmaka dari itu saya adalah murid cilsy = {muridcilsy}.\nBiaya belajar di QA Cilsy adalah {biaya:,}"

print(format_str)
print("\n")

#bilangan desimal

desimal = 123.25125324
print(f"Desimal tapi hanya 2 angka dibelakang koma: {desimal:.2f}")
print("\n")

#menampilkan leading zero

desimal = 123.25125324
print(f"Desimal tapi hanya 2 angka dibelakang koma: {desimal:5.2f}")
print(f"Desimal tapi hanya 2 angka dibelakang koma: {desimal:09.2f}")
print("\n")

#menampilkan tanda + / -
angkaminus = -10
angkaplus = 10.4323
formatminus = f"minus = {angkaminus:+}"
formatplus = f"plus = {angkaplus:+07.2f}"

print(formatminus)
print(formatplus)
print("\n")

#memformat persen
persentase = 0.045
formatpersen = f"persen = {persentase:.1%}"
print(formatpersen)
print("\n")

#melakukan operasi aritmatika dalam placeholder {}
harga = 10000
jumlah = 5
formatstr = f"Harga total = Rp.{harga*jumlah}"
print(formatstr)
print("\n")

#format angka lain seperti binary, octal, hexadecimal

angka = 255
formatbinary = f"Binary angka: {bin(angka)}"
formatoctal = f"Octal angka: {oct(angka)}"
formathex = f"Hex angka: {hex(angka)}"

print(formatbinary,"\n",formatoctal,"\n",formathex)