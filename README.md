1. Генерация запросов SQL для добавление ролей и Id ролей в таблицу keycloak_roles
- Клонируем репозиторий
- Открываем в IDE
- Создаем файл с кредами или используем существующий **config_keycloak.py**
- Указывает креды для подключения Keycloak

```
keycloak_url_m = "https://example.ru" # URL Keycloak сервера
realm_name_m = "example"  # Имя  Realm
username_m = "example"  # Имя пользователя администратора
password_m = "example"  # Пароль администратора
client_id_m = "example"  # ID клиента 
client_uuid_m = "11111111-1111-1111-1111-111111111111"
client_secret_m = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
```
- запускаем скрипт **get_role_id_gen_query.py**

2. Генерация sql запросов для маппинга ролей
- Создаем файл с кредами или используем существующий **config_db.py**
```
host = "example"
port = 5432
user = "example"
password = "example"
dbname = "example"
```
- Добавляем файл **mapping.xlsx**. Его присылает Заказчик.
При необходимости подредактировать его чтобы роли Кейклок 
были указаны в столбце excel B, роли КМС в столбце G
- запускаем **get_roles_and_mapping.py**

**connect_to_db.py** - проверка подключения к БД, выводит списк пользователей

Протестировано на версии Кейклок 22.0.0