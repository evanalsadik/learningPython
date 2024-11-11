import matplotlib.pyplot as plt

# data produk
produk = ['A', 'B', 'C', 'D', 'E', 'F' , 'G' ,'H', 'I']
jumlah = [4, 5, 6, 8, 13, 15, 11, 12, 12]

# membuat diagram garis
plt.plot(produk, jumlah)

# memberikan label pada sumbu x dan y
plt.xlabel('Nama Produk')
plt.ylabel('Jumlah Terjual')

# menampilkan diagram garis
plt.show()
