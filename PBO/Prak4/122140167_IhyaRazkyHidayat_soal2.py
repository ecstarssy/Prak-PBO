class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitungLuas(self):
        return self.sisi * self.sisi

class Lingkaran:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def hitungLuas(self):
        return 3.14 * self.jari_jari * self.jari_jari

persegi = Persegi(5)
lingkaran = Lingkaran(3)

print(f"Luas Persegi: {persegi.hitungLuas()}") 
print(f"Luas Lingkaran: {lingkaran.hitungLuas()}") 
