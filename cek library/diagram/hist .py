import matplotlib.pyplot as plt

# data produk
jumlah = [100, 80, 60, 140, 90, 110, 130, 120, 150, 170]

# membuat histogram
plt.hist(jumlah, bins=10)

# memberikan label pada sumbu x dan y
plt.xlabel('Jumlah Terjual')
plt.ylabel('Frekuensi')

# menampilkan histogram
plt.show()
