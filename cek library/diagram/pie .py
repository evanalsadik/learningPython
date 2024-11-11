import matplotlib.pyplot as plt

# data produk
produk = ['Produk A', 'Produk B', 'Produk C']
jumlah = [100, 80, 60]

# membuat pie chart
plt.pie(jumlah, labels=produk)

# menampilkan pie chart
plt.show()
