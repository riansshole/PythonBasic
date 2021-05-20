# episode latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# ++++++3--------10+++++++

inputUser = float(input("Masukkan angka yang kurang dari 3\natau \nlebih besar dari 10: \n"))

# Memeriksa angka kurang dari 3

isLessThan = (inputUser < 3)
#print("Kurang dari 3 = ", isLessThan)

# Memeriksa angka lebih dari 10

isMoreThan = (inputUser > 10)
#print("Lebih dari 10 = ", isMoreThan)

# ++++++3--------10+++++++

isCorrect = isLessThan or isMoreThan
print("Angka yang anda masukkan: ",isCorrect)

# ------3+++++++10------
#kasus irisan
print("\n", 35*"=", "\n")
inputUser = float(input("Masukkan angka yang lebih dari 3\ndan \nkurang dari 10: \n"))

# -----3++++++++++++

isMoreThan = (inputUser > 3 )
print("Lebih dari 3 : ",isMoreThan)

# +++++10-----------

isLessThan = (inputUser < 10)
print("Kurang dari 10 : ", isLessThan)

isCorrect = isMoreThan and isLessThan
print("Angka yang anda masukkan : ", isCorrect)
