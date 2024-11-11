#latihan komparasi dan logika
# === ++++3-----10++++ ===
inputuser = float(input("masukkan angka kurang dari 3 atau lebih dari 10: \n"))

#memeriksa angka < 3
iskurangdari = (inputuser < 3)
print ("angka", inputuser, "adalah kurang dari 3 = ", iskurangdari, "\ntapi")

#memeriksa angka > 10
islebihdari = (inputuser > 10)
print ("angka", inputuser, "adalah lebih dari 10 = ", islebihdari)

#memeriksa angka diluar < 3, 10 >
iscorrect = iskurangdari or islebihdari 
print ("angka yang anda masukkan : ", iscorrect, "\n")


#daerah irisan
# === ----3+++++10---- ===
inputuser2 = float(input("masukkan angka lebih dari 3 atau kurang dari 10: \n"))

#memeriksa angka > 3
islebihdari = inputuser2 > 3
print ("angka", inputuser2, "adalah lebih dari 3 = ", islebihdari)

#memeriksa angka < 10
iskurangdari = inputuser2 < 10
print ("angka", inputuser, "adalah kurang dari 3 = ", iskurangdari)

#memeriksa angka diantara 3 < x < 10 
iscorrect = iskurangdari or islebihdari 
print ("angka yang anda masukkan : ", iscorrect, "\n")





