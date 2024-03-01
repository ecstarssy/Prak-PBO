a = int(input("batas bawah : "))
b = int(input("batas atas : "))
c = 0

if(a < 0 or b < 0 ):
    print("Batas bawah dan atas tidak boleh dibawah nol")
else:
    for i in range (a,b):
        if(i%2 == 1):
            print(i)
            c += i
    print("total bilangan ganjil = " + str(c))
        
