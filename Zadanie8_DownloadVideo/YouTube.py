from pytube import YouTube

def download_video(video_url, save_path='downloads'):
    try:
        # Создание объекта YouTube
        yt = YouTube(video_url)

        # Получение самого высокого качества видео
        video = yt.streams.get_highest_resolution()

        # Создание каталога для сохранения видео
        import os
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # Загрузка видео
        video.download(save_path)

        print(f"Видео успешно скачано: {yt.title}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    video_url = 'https://www.youtube.com/watch?v=qXoRx4rmUcE'
    download_video(video_url)
