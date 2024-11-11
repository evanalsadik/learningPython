from tabulate import tabulate

# membuat data
data = [
    ['Andi', 22, 'Jakarta'],
    ['Budi', 25, 'Bandung'],
    ['Caca', 30, 'Surabaya']
]

# menampilkan tabel
print(tabulate(data, headers=['Nama', 'Usia', 'Kota']))
