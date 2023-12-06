import youtube_dl

def download_video(video_url, save_path='downloads'):
    try:
        # Создание объекта yt_dlp
        ydl = youtube_dl.YoutubeDL()

        # Установка параметров для скачивания
        options = {
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'format': 'bestvideo+bestaudio/best',
        }

        with ydl:
            result = ydl.extract_info(video_url, download=True)
            # Сохранение видео в указанное место
            ydl.download([video_url])

        print(f"Видео успешно скачано: {result['title']}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    video_url = input("Введите URL видео на RuTube: ")
    download_video(video_url)
