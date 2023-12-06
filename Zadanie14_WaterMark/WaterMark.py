import cv2

def add_watermark(input_video_path, output_video_path, watermark_path, position=(10, 10), alpha=0.8):
    # Открытие видеофайла
    cap = cv2.VideoCapture(input_video_path)

    if not cap.isOpened():
        print("Ошибка при открытии видео.")
        return

    # Получение размеров кадра
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # Загрузка водяного знака
    watermark = cv2.imread(watermark_path, cv2.IMREAD_UNCHANGED)

    # Размер водяного знака
    watermark_height, watermark_width, _ = watermark.shape

    # Создание VideoWriter для записи выходного видео
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, 20.0, (frame_width, frame_height))

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Расположение водяного знака на кадре
        roi = frame[position[1]:position[1] + watermark_height, position[0]:position[0] + watermark_width]

        # Комбинирование кадра и водяного знака с использованием альфа-канала
        frame[position[1]:position[1] + watermark_height, position[0]:position[0] + watermark_width] = \
            cv2.addWeighted(roi, 1 - alpha, watermark[:, :, :3], alpha, 0)

        # Запись кадра в выходное видео
        out.write(frame)

        # Отображение кадра с водяным знаком (необязательно)
        cv2.imshow("Watermarked Video", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Освобождение ресурсов
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_video_path = "test_1.mp4"  # Укажите путь к вашему видеофайлу
    output_video_path = "test_2.avi"  # Укажите имя для выходного видеофайла
    watermark_path = "WaterMark.png"  # Укажите путь к вашему водяному знаку

    # Задайте позицию водяного знака и прозрачность
    watermark_position = (10, 10)
    alpha = 0.8

    add_watermark(input_video_path, output_video_path, watermark_path, watermark_position, alpha)
