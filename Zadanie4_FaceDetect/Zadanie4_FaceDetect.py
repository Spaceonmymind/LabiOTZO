import cv2
import face_recognition
from deepface import DeepFace


def detect_faces(image_path):
    # Загрузка изображения
    image = cv2.imread(image_path)

    # Инициализация детектора лиц
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Отрисовка прямоугольника вокруг обнаруженного лица
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

        # Определение возраста, эмоций и расы
        face = DeepFace.analyze(image_path, actions=['age', 'emotion', 'race'])

        # Вывод результатов
        print(f"Возраст: {face['age']}")
        print(f"Эмоция: {face['dominant_emotion']}")
        print(f"Раса: {face['dominant_race']}")

    # Отображение результата
    cv2.imshow("Detected Faces", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    image_path = "img.jpg"
    detect_faces(image_path)
