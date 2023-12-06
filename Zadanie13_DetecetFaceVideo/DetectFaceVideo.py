import cv2
import dlib
import imghdr

def is_video(file_path):
    # Используем imghdr, чтобы определить тип файла
    file_type = imghdr.what(file_path)
    return file_type and file_type.startswith('video')

# Загрузка предобученного детектора лиц из dlib
detector = dlib.get_frontal_face_detector()

# Запуск камеры или видеофайла
video_path = "your_video.mp4"  # Укажите путь к вашему видеофайлу
cap = cv2.VideoCapture(0) if video_path is None else cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Ошибка при открытии видео.")
    exit()

while True:
    # Захват кадра с камеры или видео
    ret, frame = cap.read()

    if not ret:
        print("Не удалось получить кадр.")
        break

    # Конвертация в оттенки серого для улучшения производительности
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Детекция лиц
    faces = detector(gray)

    # Отрисовка прямоугольников вокруг лиц
    for face in faces:
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Отображение кадра
    cv2.imshow("Face Detection", frame)

    # Прерывание цикла по нажатию клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождение ресурсов
cap.release()
cv2.destroyAllWindows()
