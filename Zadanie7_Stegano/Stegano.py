from PIL import Image

def encode_text_into_image(text, input_image_path, output_image_path):
    # Открытие изображения
    img = Image.open(input_image_path)

    # Преобразование текста в бинарную строку
    binary_text = ''.join(format(ord(char), '08b') for char in text)

    # Получение списка пикселей изображения
    pixels = list(img.getdata())

    # Замена последних бит каждого канала RGB на биты текста
    new_pixels = []
    for i, pixel in enumerate(pixels):
        new_pixel = list(pixel)
        for j in range(3):  # Три канала: R, G, B
            if i * 3 + j < len(binary_text):
                new_pixel[j] = (new_pixel[j] & 0b11111110) | int(binary_text[i * 3 + j])
        new_pixels.append(tuple(new_pixel))

    # Создание нового изображения с палитрой RGB
    new_img = Image.new("RGB", img.size)
    new_img.putdata(new_pixels)
    new_img.save(output_image_path)

def decode_text_from_image(input_image_path):
    # Открытие изображения
    img = Image.open(input_image_path)

    # Получение списка пикселей изображения
    pixels = list(img.getdata())

    # Извлечение бит текста из последних бит каждого канала RGB
    binary_text = [str(pixel[j] & 1) for pixel in pixels for j in range(3)]

    # Разделение бинарной строки на 8-битные символы
    text = ''.join([chr(int(''.join(binary_text[i:i+8]), 2)) for i in range(0, len(binary_text), 8)])

    return text

if __name__ == "__main__":
    # Пример использования
    text_to_hide = "Hello, this is a secret message!"
    input_image_path = "img2.png"
    output_image_path = "img3.png"

    # Сокрытие текста в изображении
    encode_text_into_image(text_to_hide, input_image_path, output_image_path)

    # Извлечение текста из изображения
    extracted_text = decode_text_from_image(output_image_path)
    print(f"Извлеченный текст: {extracted_text}")
