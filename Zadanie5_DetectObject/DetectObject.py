import cv2


def detect_objects(image_path, cascade_path):
    # Загрузка изображения
    image = cv2.imread(image_path)

    # Преобразование изображения в оттенки серого (требуется для метода каскадов Хаара)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Загрузка каскада Хаара для объекта, который вы хотите обнаружить
    cascade = cv2.CascadeClassifier(cascade_path)

    # Обнаружение объектов
    objects = cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Отрисовка прямоугольников вокруг обнаруженных объектов
    for (x, y, w, h) in objects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Отображение результата
    cv2.imshow("Detected Objects", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    image_path = "img1.jpg"
    cascade_path = "haarcascade_eye.xml"  # Путь к файлу каскада Хаара
    detect_objects(image_path, cascade_path)
