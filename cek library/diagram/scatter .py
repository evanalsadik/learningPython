import matplotlib.pyplot as plt

# data produk
harga = [25000, 35000, 45000]
jumlah = [100, 80, 60]

# membuat scatter plot
plt.scatter(harga, jumlah)

# memberikan label pada sumbu x dan y
plt.xlabel('Harga')
plt.ylabel('Jumlah Terjual')

# menampilkan scatter plot
plt.show()
