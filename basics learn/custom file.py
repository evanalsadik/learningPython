file = open("//storage//emulated//0//ASD/file_baru.txt", "r")
text = file.read()
print (text)
file.close()

# "r" bisa di ubah menjadi 
# 1). "x" untuk mengecek nama folder jika sudah ada, folder tak akan dicetak.
# 2). "w" untuk memasukkan teks baru.
# 3). "a" untuk menambah teks baru.
# 4). "r" untuk membaca teks tanpa membuka file.