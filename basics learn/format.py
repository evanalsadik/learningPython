##format

# string
nama = "damar"
format_str = f"hallo {nama}" 
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}" 
print(format_str)

# angka
#bilangan bulat
angka = 17
format_str = f"bilangan bulat = {angka:d}" 
# (d tidak terlalu berpengaruh)
print(format_str)

#bilangan ribuan
ribuan = 66368760000
format_str = f"ribuan = {ribuan:,}" 
# (tanda , untuk memisahkan 3 angka supaya jadi ribuan (rapih))
print(format_str)

#bilangan desimal
desimal = 6636876.8377393
format_str = f"desimal = {desimal:.3f}" 
# (angka 3 untuk menentukan jumlah angka dibelakanng koma)
print(format_str)

# leading zero
desimal2 = 6636876.8377393
format_str = f"desimal.2 = {desimal2:0010.3f}" 
print(format_str) 

# menambahkan tanda + -
angkaMinus = -12
angkaPlus = 12
formatAm = f"angka minus = {angkaMinus:+d}"
formatAp = f"angka plus = {angkaPlus:+d}"
# (+d untuk menampilkan +/- yang asalnya tudak terlihat)
print (formatAm)
print (formatAp)

# format persen
persentase = 0.736
formatP = f"persentase {persentase:.2%}"
# (.2 menunjukkan jumlah angka dibelakang koma dan % menunjukkan persen yang asalnya tidak ada)
print (formatP)

#operasi aritmatika dalam placeholder
harga = 5000
jumlah = 7
formatStr = f"harga total = rp. {harga * jumlah:,}"
print(formatStr)

# format angka lain (binary, octal, hexadecimal)
angka = 255
formatBinary = f"binary = {bin(angka)}"
formatOctal = f"octal = {oct(angka)}"
formatHex = f"hexadecimal = {hex(angka)}"
print (formatBinary)
print (formatOctal)
print (formatHex)




