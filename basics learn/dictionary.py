siswa = {"nama":"tatang", "umur":17, "kelas":"XII", "alamat":"pengkolan"}

#jumlah item
jumlah_item = len(siswa)
print("jumlah item: ", jumlah_item, "\n")

#menambah item
siswa["cita-cita"] = "koruptor"
siswa["tinggi badan"] = "70 cm"
print("menambah: ", siswa, "\n")

#mengganti value
siswa["alamat"] = "mars"
print("mengganti value: ", siswa, "\n")

#menghapus item
siswa.pop("tinggi badan")
print("menghapus: ", siswa, "\n")

del siswa["alamat"]
print("menghapus1: ", siswa, "\n")

#danger
#siswa.clear()
#print("menghapus semua item: ", siswa, "\n")

#del siswa
#print("menghapus keseluruhan: ", siswa, "\n")

#akses & for loop
key = siswa.keys()
print("\nakses key only: ", key, "\n")

value = siswa.values()
print("akses value only: ", value, "\n")

item = siswa.items()
print("akses keduanya: ", item, "\n")

#for loop
print("\nkey: ")
for i in key:
    print(i)
    
print("\n\nvalue: ")
for i in value:
    print(i)
    
print("\n\nfull item: ")
for k,v in item:
    print(k,v)