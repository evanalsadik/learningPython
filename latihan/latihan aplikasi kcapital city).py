negara = ["indonesia", "jepang", "amerika", "china", "jerman", "inggris", "russia"]
ibukota = ["Jakarta", "Tokyo", "Washington DC", "Beijing", "Berlin", "London", "Moscow"]

capital_city = dict(zip(negara, ibukota))

while True:
    nama_negara = input("negara: ").lower()
    nama_ibukota = capital_city[nama_negara]
    print ("ibu kota", nama_negara.title(), "adalah: ", nama_ibukota, end="\n\n")