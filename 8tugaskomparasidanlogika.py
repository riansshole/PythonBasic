#Tugas

print("\n",30*"=","\n")
inputUser = (float(input("Masukkan angka dari 0 hingga 50: ")))
#-----0++++++10------20+++++++50-----

var1 = inputUser>0
var2 = inputUser<10
hasil1 = var1 or var2

var3 = inputUser>20
var4 = inputUser<50
hasil2 = var3 or var4

seluruhan = hasil1 and hasil2
print("Hasil seluruhan: ",seluruhan)

#+++++0------10++++++20-------50+++++
print("\n",30*"=","\n")
inputUser = float(input("Masukkan angka dari 0 hingga 50: "))

variable1 = inputUser<0
variable2 = inputUser>10
hasil1 = variable1 or variable2

variable3 = inputUser<20
variable4 = inputUser>50
hasil2 = variable3 or variable4

Seluruh = hasil1 and hasil2

print("Hasil seluruh: ",Seluruh)