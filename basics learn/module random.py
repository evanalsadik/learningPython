import random

#nama acak
nama_siswa = ("budi", "budiman", "mamat", "damar", "jamal", "abdul")

acak_nama = random.choice(nama_siswa)

print (acak_nama)


#angja acak
angka_acak = random.randrange(9999999999999)

print (angka_acak)


#integer acak
angka_acak2 = random.randint(200, 288)

print (angka_acak2)


#list acak
x = [1,2,3,4,5,6,7,8,9,10]

angka_acak3 = random.shuffle(x)

print (x)


#mengacak angka float 0-1
print(random.random())