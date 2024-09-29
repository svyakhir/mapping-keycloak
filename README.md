**Для генерации запросов, добавления ролей из кейклок в БД KMS выполнить:**
1. В файл config_keycloak.py указать креды для подключения к Кейклок
2. Для запуска основного файла get_role_id_gen_query.py требуются
файлы config_keycloak.py и get_token_keycloak.py откуда берутся функции и креды
3. Запустить get_role_id_gen_query.py в IDE. Он выдаст подготовленые запросы
для выполнения в БД

Для генерации запросов сопоставления ролей КМС и Кейклок (get_role_id_gen_query.py) 
используется файл mapping.xlsx. Обычно его присылает Заказчик.
Роли Кейклок должны быть указаны в столбце excel B, роли КМС в
столбце G