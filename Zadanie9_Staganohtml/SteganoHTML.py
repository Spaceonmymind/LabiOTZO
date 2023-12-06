def hide_data_in_html(input_file, output_file, secret_data):
    try:
        # Чтение HTML-файла
        with open(input_file, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Преобразование текста в бинарную строку
        binary_secret_data = ''.join(format(ord(char), '08b') for char in secret_data)

        # Встраивание битов текста в комментарии HTML
        encoded_html_content = html_content
        for i, bit in enumerate(binary_secret_data):
            comment_start = f"<!--_{i}_"
            comment_end = "_-->"
            encoded_html_content = encoded_html_content.replace(comment_start, comment_start + bit + comment_end)

        # Запись измененного HTML-файла
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(encoded_html_content)

        print("Данные успешно спрятаны в HTML-файле.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def extract_data_from_html(input_file):
    try:
        # Чтение измененного HTML-файла
        with open(input_file, 'r', encoding='utf-8') as file:
            encoded_html_content = file.read()

        # Извлечение битов текста из комментариев HTML
        binary_secret_data = ""
        i = 0
        while True:
            comment_start = f"<!--_{i}_"
            comment_end = "_-->"
            start_index = encoded_html_content.find(comment_start)
            end_index = encoded_html_content.find(comment_end, start_index)
            if start_index == -1 or end_index == -1:
                break
            bit = encoded_html_content[start_index + len(comment_start):end_index]
            binary_secret_data += bit
            i += 1

        # Преобразование бинарной строки в текст
        extracted_data = ''.join([chr(int(binary_secret_data[i:i+8], 2)) for i in range(0, len(binary_secret_data), 8)])

        print(f"Извлеченные данные: {extracted_data}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    input_html_file = "example.html"
    output_html_file = "example1.html"
    secret_text = "12312Text"

    hide_data_in_html(input_html_file, output_html_file, secret_text)
    extract_data_from_html(output_html_file)
