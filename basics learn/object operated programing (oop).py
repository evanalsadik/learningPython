class cat():
    def __init__(self, nama, umur, warna):
        self.nama = nama
        self.umur = umur
        self.warna = warna

    def speak(self):
        print("meow, meow, meow")
        
    def eat(self):
        print("aug, aug, aug")

mycat = cat("artur", 2, "black")
nana = cat("nana", 1, "biru")

print(mycat.nama)
print(mycat.warna)
print(mycat.umur)

mycat.speak()
mycat.eat()

print(nana.nama)
print(nana.warna)
print(nana.umur)