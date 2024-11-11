from prettytable import PrettyTable

# membuat tabel
table = PrettyTable(['Nama', 'Usia', 'Kota'])
table.add_row(['Andi', 22, 'Jakarta'])
table.add_row(['Budi', 25, 'Bandung'])
table.add_row(['Caca', 30, 'Surabaya'])

# menampilkan tabel
print(table)
