from get_token_keycloak import *
from config_keycloak import realm_name_m
token = get_token_keycloak()

# Получение списка ролей Клиента
roles_list_url = f"{keycloak_url_m}/admin/realms/{realm_name_m}/clients/{client_uuid_m}/roles"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

response = requests.get(roles_list_url, headers=headers)
roles = response.json()
for role in roles:
    print(f"{role['name']}: {role['id']}")