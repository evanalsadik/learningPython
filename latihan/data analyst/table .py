from prettytable import PrettyTable

# membuat tabel
table = PrettyTable(['Nama Produk', 'Harga', 'Jumlah Terjual'])
table.add_row(['Produk A', 25000, 100])
table.add_row(['Produk B', 35000, 80])
table.add_row(['Produk C', 45000, 60])

# menampilkan tabel
print(table)
