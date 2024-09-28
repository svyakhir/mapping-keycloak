from get_token_keycloak import *
from config_keycloak import realm_name_m
token = get_token_keycloak()

def get_role_id_name():
    # Получение списка ролей Клиента
    roles_list_url = f"{keycloak_url_m}/admin/realms/{realm_name_m}/clients/{client_uuid_m}/roles"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.get(roles_list_url, headers=headers)
    roles = response.json()

    # Список для хранения результатов
    result = []

    for role in roles:
        result.append(f"insert into keycloak_roles (keycloak_id, name) values ('{role['id']}', '{role['name']}');")

    return '\n'.join(result)

print(f"\n{get_role_id_name()}")