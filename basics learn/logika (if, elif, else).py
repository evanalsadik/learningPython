#logika
galaksi = input("kita ada di galaksi apa: ")

if galaksi == "milky way":
    print("benar")
elif galaksi == "andromeda":
    print("mendekati")
else:
    print("bukan")
    
    
#logika (nested -if)
umur = 25
pendidikan_terakhir = "s3"

if umur >= 20 and umur <=35:
    if pendidikan_terakhir == "s1" or pendidikan_terakhir == "s2" or pendidikan_terakhir == "s3":
        print("selamat anda diterima diperusahaan ini")
else:
    print("maaf anda tidak diterima")