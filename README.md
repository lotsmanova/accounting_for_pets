# Accounting for pets

---

REST API для ведения учета питомцев (собак и кошек).

## Технологии

---

- Python 3+
- FastAPI
- PostgreSQL
- Pydantic
- SQLAlchemy

## Запуск проекта

---

- Зависимости для проекта находятся в `requirements.txt`. Команда для установки: `pip install -r requirements.txt`;
- Файл `.env.sample` содержит необходимые переменные окружения;
- Применить миграции: `alembic upgrade head`

## Структура проекта

---

**API Key Authentication**

Все  endpoints защищены API Key Authentication. Чтобы получить доступ к сервису, необходимо аутентифицироваться эталонным API_KEY.

**Endpoints**:

- [ ]  `/pets`.  post-запрос для создания питомца.
- [ ]  `/pets`. get-запрос для получения информации о питомцах в виде списка.
- [ ]  `/pets/{id}`.  delete-запрос для удаления питомцев. На вход передается список id питомцев.
- [ ]  `/pets/{id}/photo`. post-запрос для добавления фотографий питомца.

**Модели SQLAlchemy:**

- [ ]  `Pets`. Структура таблицы для хранения информации о питомцах в базе данных.
- [ ]  `Photos`. Структура таблицы для хранения фотографий питомца в базе данных.

Связь между таблицами один ко многим. 

**Схемы Pydantic:**

- [ ]  `PetAdd` и `PetRead`. Создание и просмотр питомцев соответственно.
- [ ]  `PhotoBase` и `PhotoRead`. Создание и просмотр фотографий соответственно.

**Кастомная команда**

Чтобы получить список питомцев в терминале, воспользуйтесь командой: 

 `python3 src.pets_export.py`

Чтобы получить питомцев только с фотографиями, добавьте к команде `true`. Чтобы получить питомцев без фотографий, добавьте к команде `false`.

## Документация

---

Документация к API доступна по ссылке http://127.0.0.1:8000/docs/

## Тестирование

---

Тесты написаны с помощью библиотеки `pytest`. Общее покрытие тестами  78 %.

## Docker

---

Сбор контейнера: `docker compose build`

Запуск контейнера: `docker compose up`