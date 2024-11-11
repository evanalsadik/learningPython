print ("\nOprrasi hitung / kalkulator python.")
print ("Pilih tanda [+] untuk operasi pertambahan")
print ("Pilih tanda [-] untuk operasi pengurangan")
print ("Pilih tanda [*] untuk operasi perkalian")
print ("Pilih tanda [**] untuk operasi perpangkatan")
print ("Pilih tanda [/] untuk operasi pembagian")
print ("Pilih tanda [//] untuk operasi pembagian tanpa hasil desimal")
print ("Pilih tanda [%] untuk operasi mencari sisa bagi")

while True:
    operasi = input("\nTentukan operasi yang ingin anda gunakan! ")
    if operasi not in ("+", "-", "*", "**", "/", "//", "%"):
        print("Lu salah masukin simbol bego!1!1!")
        break
    
    x = int(input("\nmasukkan angka pertama: "))
    y = int(input("masukkan angka ke dua: "))
    
    if operasi == "+":
        print ("\nhasil dari", x, "+", y, "=", x+y)
    elif operasi == "-":
        print ("\nhasil dari", x, "-", y, "=", x-y)
    elif operasi == "*":
        print ("\nhasil dari", x, "*", y, "=", x*y)
    elif operasi == "**":
        print ("\nhasil dari", x, "**", y, "=", x**y)
    elif operasi == "/":
        print ("\nhasil dari", x, "/", y, "=", x/y)
    elif operasi == "//":
        print ("\nhasil dari", x, "//", y, "=", x//y)
    elif operasi == "%":
        print ("\nhasil dari", x, "%", y, "=", x%y)