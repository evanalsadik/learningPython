import matplotlib.pyplot as plt

# data produk
produk = ['Produk A', 'Produk B', 'Produk C']
jumlah = [100, 80, 60]

# membuat bar chart
plt.bar(produk, jumlah)

# memberikan label pada sumbu x dan y
plt.xlabel('Nama Produk')
plt.ylabel('Jumlah Terjual')

# menampilkan bar chart
plt.show()
