import requests
from config_keycloak import *

import requests

# Параметры подключения
keycloak_url = "http://localhost:8080/auth/realms/master/protocol/openid-connect/token"
realm_name = "your_realm"

# Получение токена
data = {
    "client_id": client_id_m,
    "username": username_m,
    "password": password_m,
    "grant_type": "password"
}

response = requests.post(keycloak_url_m, data=data)
token = response.json()["access_token"]
