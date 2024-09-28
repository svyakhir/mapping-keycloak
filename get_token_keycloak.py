import requests
from config_keycloak import *

# Параметры подключения
keycloak_url = f"{keycloak_url_m}/realms/{realm_name_m}/protocol/openid-connect/token"

# Получение токена
def get_token_keycloak():
    data = {
        "client_id": client_id_m,
        "username": username_m,
        "password": password_m,
        "grant_type": "password"
    }

    # Отправка POST-запроса для получения токена
    response = requests.post(keycloak_url, data=data)

    # Вывод отладочной информации
    # print("Request URL:", response.request.url)
    # print("Request Headers:", response.request.headers)
    # print("Request Body:", response.request.body)
    # print("Status Code:", response.status_code)
    # print("Response Text:", response.text)

    # Проверка успешности запроса
    if response.status_code == 200:
        token_info = response.json()  # Получаем данные в формате JSON
        access_token = token_info.get('access_token')  # Извлекаем access_token
        return access_token
        # print(f"{access_token}")
        # print(token_info)
    else:
        return  f"Ошибка получения токена: {response.status_code}. Для дополнительной информации испльзуйте вывод " \
                f"отладочной информации"
