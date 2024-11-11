import os
import re

# Tentukan folder yang berisi file musik
folder_path = '/home/left/Music/Musics/'

# Buat file TXT baru
txt_file = 'music_filess.txt'

# Dapatkan daftar file di dalam folder
file_names = os.listdir(folder_path)

# Filter file yang memiliki ekstensi musik (misalnya .mp3)
music_files = [f for f in file_names if f.endswith('.mp3')]

# Regex untuk memisahkan penyanyi, judul lagu, dan ft (jika ada)
pattern = re.compile(r'^(.*?) - (.*?) ?(?:\[ft. (.*?)\])?\.mp3$', re.IGNORECASE)

# Simpan data musik ke dalam list untuk diurutkan
music_data = []

for music_file in music_files:
    match = pattern.match(music_file)
    if match:
        penyanyi = match.group(1)
        judul_lagu = match.group(2)
        ft = match.group(3) if match.group(3) else ''  # Bisa kosong jika tidak ada "ft."
        if ft:
            music_data.append(f'{penyanyi} - {judul_lagu} (ft. {ft})')
        else:
            music_data.append(f'{penyanyi} - {judul_lagu}')

# Urutkan berdasarkan nama penyanyi (karena formatnya "Penyanyi - Judul Lagu")
music_data_sorted = sorted(music_data)

# Tulis ke file TXT
with open(txt_file, mode='w') as file:
    for entry in music_data_sorted:
        file.write(f'{entry}\n')

print(f'File TXT berhasil dibuat dan disusun A-Z: {txt_file}')
