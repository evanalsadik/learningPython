x = ["ikan", "hiu", "paus", "kepiting", "bintang laut", "kura-kura", "pari"]

#jumlah item
item = len(x)
print("jumlah: ", item) 

#mencari item lewat nomor index
idx = x[0]
print("\ndepan: ", idx)

idxa = x[-1]
print("\nbelakang: ", idxa, "\n")

#~~~ index rentang
idx_1 = x[1:3] 
print("\nrentang: ", idx_1)

idx_1a = x[1:]
print(idx_1a, "\n")

#~~~ index step (bilangan kelipatan)
idx_2 = x[0::2]
print("\nkelipatan: ", idx_2)

#~~~ index batas
idx_3 = x[0:5:3]
print("\nbatas: ", idx_3, "\n")

#penambahan item
x.append ("gurita")
x.append ("penguin")
print("penambahan: ", x)

#~~~ tersusun
x.insert(1, "fred my leg")
x.insert(3, "salmon")
print("tersusun: ", x, "\n")

#mengganti item
x[2] = "singa"
x[1] = "gajah"
print("mengganti: ", x, "\n")

#menghapus item dengan index / nama item
x.pop(5)
print("menghapus lewat index: ", x)

del x[1]
print("sama dengan yang atas:", x)

x.remove("pari")
print("menghapus lewat string: ", x)

x.clear()
print("menghapus semua isi variable: ", x)
