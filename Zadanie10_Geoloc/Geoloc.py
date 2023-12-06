import requests


def get_location_by_ip(ip_address):
    try:
        # Запрос к API ipinfo.io
        response = requests.get(f"http://ipinfo.io/{ip_address}/json")

        # Парсинг ответа в формате JSON
        data = response.json()

        # Вывод информации о геолокации
        print("Геолокация по IP-адресу {}: ".format(data.get('ip')))
        print("Страна: {}".format(data.get('country')))
        print("Регион: {}".format(data.get('region')))
        print("Город: {}".format(data.get('city')))
        print("Широта: {}".format(data.get('loc').split(',')[0]))
        print("Долгота: {}".format(data.get('loc').split(',')[1]))
    except Exception as e:
        print("Произошла ошибка: {}".format(e))


def get_own_ip_and_location():
    try:
        # Запрос к API для получения текущего IP-адреса
        response = requests.get("https://api64.ipify.org?format=json")

        # Парсинг ответа в формате JSON
        data = response.json()

        own_ip = data.get('ip')
        print("Ваш текущий IP-адрес: {}".format(own_ip))

        # Получение геолокации по текущему IP-адресу
        get_location_by_ip(own_ip)
    except Exception as e:
        print("Произошла ошибка: {}".format(e))


if __name__ == "__main__":
    get_own_ip_and_location()
