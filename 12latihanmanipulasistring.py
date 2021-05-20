def kali():
    kali= input ("pilihlah perkalian dari 1-10\nbatal\n:")
    return kali

while True:
    a= kali()
    if a== "1":
        for x in range(1,11,1):
            print(x)
    elif a== "2":
        for x in range(2,21,2):
            print(x)
    elif a== "3":
        for x in range(3,31,3):
            print(x)
    elif a== "4":
        for x in range(4,41,4):
            print(x)
    elif a== "5":
        for x in range(5,51,5):
            print(x)
    elif a== "6":
        for x in range(6,61,6):
            print(x)
    elif a== "7":
        for x in range(7,71,7):
            print(x)
    elif a== "8":
        for x in range(8,81,8):
            print(x)
    elif a== "9":
        for x in range(9,91,9):
            print(x)
    elif a== "10":
        for x in range(10,101,10):
            print(x)
    elif a== "batal":
        break
    else:
        print("\noperasi tidak diketahui, silahkan coba lagi\n")