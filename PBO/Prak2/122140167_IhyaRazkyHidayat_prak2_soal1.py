class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        self.nim = nim
        self.nama = nama
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa
    
    # Getter untuk nim
    def getNIM(self):
        return self.nim
    
    # Setter untuk nim
    def setNIM(self, nim):
        self.nim = nim
    
    # Getter untuk nama
    def getNama(self):
        return self.nama
    
    # Setter untuk nama
    def setNama(self, nama):
        self.nama = nama
    
    # Method 1: Contoh operasi sederhana
    def method1(self):
        return f"{self.nama} sedang belajar."
    
    # Method 2: Contoh operasi sederhana
    def method2(self):
        return f"{self.nama} sedang mengikuti kuliah."
    
    # Method 3: Contoh operasi sederhana
    def method3(self):
        return f"{self.nama} adalah mahasiswa angkatan {self.angkatan}."


# Inisiasi objek pertama
mahasiswa1 = Mahasiswa("123456", "John Doe", 2022)

# Inisiasi objek kedua
mahasiswa2 = Mahasiswa("654321", "Jane Smith", 2023)

# Penggunaan objek pertama
print("Objek 1:")
print("NIM:", mahasiswa1.getNIM())
print("Nama:", mahasiswa1.getNama())
print("Angkatan:", mahasiswa1.angkatan)
print("Apakah mahasiswa:", mahasiswa1.isMahasiswa)
print(mahasiswa1.method1())
print(mahasiswa1.method2())
print(mahasiswa1.method3())

print("\nObjek 2:")
# Penggunaan objek kedua
print("NIM:", mahasiswa2.getNIM())
print("Nama:", mahasiswa2.getNama())
print("Angkatan:", mahasiswa2.angkatan)
print("Apakah mahasiswa:", mahasiswa2.isMahasiswa)
print(mahasiswa2.method1())
print(mahasiswa2.method2())
print(mahasiswa2.method3())
