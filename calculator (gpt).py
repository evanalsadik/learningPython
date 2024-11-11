# Definisikan fungsi untuk setiap operasi matematika
def tambah(x, y):
   return x + y

def kurang(x, y):
   return x - y

def kali(x, y):
   return x * y

def bagi(x, y):
   return x / y

# Menampilkan pilihan menu untuk pengguna
print("Pilih operasi.")
print("1.Tambah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")

# Minta pengguna memilih operasi
pilihan = input("Masukkan pilihan(1/2/3/4): ")

# Minta pengguna memasukkan angka
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

# Lakukan operasi yang dipilih oleh pengguna
if pilihan == '1':
   print(angka1,"+",angka2,"=", tambah(angka1,angka2))

elif pilihan == '2':
   print(angka1,"-",angka2,"=", kurang(angka1,angka2))

elif pilihan == '3':
   print(angka1,"*",angka2,"=", kali(angka1,angka2))

elif pilihan == '4':
   print(angka1,"/",angka2,"=", bagi(angka1,angka2))
else:
   print("Input tidak valid")
