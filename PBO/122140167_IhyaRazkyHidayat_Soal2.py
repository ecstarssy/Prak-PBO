jari2 = int(input("Masukkan jari - jari : "))
pi = 3.14

if(jari2 < 0):
    print ("Jari-jari lingkaran tidak boleh negatif")
else:
    Keliling = pi * jari2 * 2
    Luas = pi * jari2 * jari2
    print ("Luas lingkaran = " + str(Luas))
    print ("Keliling lingkaran = " + str(Keliling))

    