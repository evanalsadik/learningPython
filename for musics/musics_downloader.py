import yt_dlp

# Masukkan URL playlist YouTube Anda
playlist_url = "https://youtube.com/playlist?list=PL4O69WLuIcbrkWC9bId54Ey06-uwBn-oH&si=VspJqSgx3oA6SCQC"

# Direktori penyimpanan
output_dir = "./for musics/files/Music"

# Opsi yt-dlp
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': './Music/%(title)s.%(ext)s',
    'keepvideo': False,  # Hapus file asli setelah konversi
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    # Mendapatkan informasi playlist
    playlist_info = ydl.extract_info(playlist_url, download=False)

    # Mendapatkan daftar ID video
    video_ids = [video["id"] for video in playlist_info["entries"]]

    # Mendownload audio MP3
    for video_id in video_ids:
        try:
            # Mendapatkan judul video
            video_details = ydl.extract_info(video_id, download=False)
            title = video_details["title"]

            # Download audio
            ydl.download([video_id])
        except Exception as e:
            print(f"Gagal download video {video_id}: {e}")

print("Proses download selesai!")
