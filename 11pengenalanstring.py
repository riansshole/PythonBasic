data = "ini adalah string"
print(data)
print(type(data))

#Cara membuat string

#1. dengan menggunakan single quote '...'
print("\n",15*"=","SINGLE QUOTE",15*"=")
data = 'menggunakan single quote'
print(data)
print(type(data))

print("\n",15*"=","DOUBLE QUOTE",15*"=")
data = "menggunakan double quote"
print(data)
print(type(data))

#2. dengan menggunakan backlash \

print("\n",15*"=","BACKLASH",15*"=")
data = 'jangan lupa solat jum\'at'
print(data)
print('g\'day, mate!')
print('y\'all')
print(type(data))
lokasi = "C:\\user\\Ucup"
print(lokasi)

#. dengan menggunakan tab \t

print("\n",15*"=","TAB",15*"=")
data = "ucup \t\t\totong, jauhan"
print(data)

#. dengan menggunakan backspace \b ##SANGAT JARANG TERPAKAI

print("\n",15*"=","BACKSPACE",15*"=")
data = "ucup \botong, deketan"
print(data)

#. dengan menggunakan new line \n

print("\n",15*"=","NEW LINE",15*"=")
print("baris pertama. \nbaris kedua.") # LF -> line feed -> Unix, macos, linux
print("baris pertama. \rbaris kedua.") # CR -> carriage return -> commodore, acorn, lisp
print("baris pertama. \r\nbaris kedua.") #CRLF -> line feed carriage return -> windows

# STRING LITERAL ATAU RAW

print("\n",15*"=","RAW STRING",15*"=")

#hati hati
print('C:\new Folder')
#bisa menggunakan raw string jadi seperti ini
print(r'C:\new folder') #raw akan menghilangkan semua konversi

# Multi line literal string
print("\n",15*"=","MULTI LINE LITERAL STRING",15*"=")

print("""
Nama\t: Ucup
Kelas\t: 3 SD
Umur\t: 6 tahun
""")

# Raw multi line literal string
print("\n",15*"=","RAW MULTI LINE LITERAL STRING",15*"=")
print(r"""
Nama    : Ucup
Umur    : 22 tahun
Website : https://www.ucupgoesviral.com
""")