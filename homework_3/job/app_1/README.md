## Для доработки проекта требуется добавить: 

1. Импорт хеширования
> from werkzeug.security import generate_password_hash, check_password_hash

2. принцип работы хеширования
> Хеширование в БД
> hash = generate_password_hash("12345")

> Чтение из БД
> check_password_hash(hash, "12345")