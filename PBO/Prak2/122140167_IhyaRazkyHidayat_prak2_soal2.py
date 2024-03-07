# Kelas yang merepresentasikan sebuah mobil
class Mobil:
    def __init__(self, merek, model):
        self.merek = merek
        self.model = model
        print(f"{self.merek} {self.model} diproduksi.")

    def __del__(self):
        print(f"{self.merek} {self.model} sudah tidak dipakai lagi.")


# Decorator untuk mengecek status bahan bakar
def cek_bahan_bakar(func):
    def wrapper(self, *args, **kwargs):
        if self.bahan_bakar > 0:
            func(self, *args, **kwargs)
        else:
            print(f"{self.merek} {self.model} kehabisan bahan bakar!")
    return wrapper



class Pengemudi:
    def __init__(self, nama, mobil):
        self.nama = nama
        self.mobil = mobil
        self.bahan_bakar = 30

    @cek_bahan_bakar
    def pergi(self, tujuan):
        print(f"{self.nama} pergi ke {tujuan} dengan {self.mobil.merek} {self.mobil.model}.")

    @cek_bahan_bakar
    def pulang(self, rumah):
        print(f"{self.nama} pulang ke {rumah} dengan {self.mobil.merek} {self.mobil.model}.")


# Penggunaan kelas Mobil
mobil1 = Mobil("Toyota", "Avanza")
mobil2 = Mobil("Honda", "Jazz")

# Penggunaan kelas Pengemudi
pengemudi1 = Pengemudi("John", mobil1)
pengemudi2 = Pengemudi("Jane", mobil2)

# Pengemudi pergi dan pulang
pengemudi1.pergi("kantor")
pengemudi2.pergi("mall")

pengemudi1.pulang("rumah")
pengemudi2.pulang("apartemen")
