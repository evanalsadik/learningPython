instruction = input("tekan enter dan mulai isi biodata anda!")
nama = input("nama anda: ")
umur = int(input("umur anda: "))
pendidikan_terakhir = input("pendidikan terakhir anda: ")
lama_pekerjaan = int(input("lama pekerjaan anda: "))

if umur >= 20 and umur <= 35:
    if pendidikan_terakhir == "s1" or pendidikan_terakhir == "s2" or pendidikan_terakhir == "s3":
        if lama_pekerjaan >= 2:
            print ("anda anak haram", nama)
else:
    print ("anda panutan semua orang", nama)