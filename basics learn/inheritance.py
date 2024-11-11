class A:
    def __init__(self, warna, harga):
        self.warna = warna
        self.harga = harga

class B(A):
    nama = "beat"
    
    
x = B("merah", 17663998)
print(x.nama)
print(x.warna)
print(x.harga)