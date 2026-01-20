# 🧠 Habit Tracker — Сервис привычек с напоминаниями и Telegram-интеграцией

**Habit Tracker** — это Django REST API-сервис для создания, отслеживания и напоминания о полезных и приятных привычках.  
Пользователь может формировать собственные привычки, получать ежедневные напоминания в Telegram и просматривать публичные привычки других пользователей.

---

## 🚀 Основные функции

- ✅ CRUD-операции с привычками  
- 🔔 Ежедневные напоминания через **Telegram-бота**  
- 🔁 Периодичность выполнения (по умолчанию ежедневно)  
- 🕒 Контроль времени выполнения (до 120 секунд)  
- 💬 Приятные и полезные привычки (связанные привычки)  
- 🔒 Авторизация через **JWT**  
- 🌐 Поддержка **CORS** для фронтенда  
- 📄 Документация **Swagger / OpenAPI**  
- ⚙️ Отложенные задачи через **Celery + Redis**  
- 🧩 Тесты Pytest и оформление по **PEP8 / flake8**

---

## 🏗️ Технологический стек

| Компонент | Версия | Описание |
|------------|--------|-----------|
| **Python** | 3.13 | язык разработки |
| **Django** | 6.0.1 | веб-фреймворк |
| **Django REST Framework** | latest | REST API |
| **PostgreSQL** | 17.x | основная база данных |
| **Redis** | 7.x | брокер сообщений для Celery |
| **Celery** | 5.6.2 | планировщик задач |
| **DRF Spectacular** | latest | автогенерация Swagger-документации |
| **django-cors-headers** | 4.9.0 | поддержка CORS |
| **pytest / pytest-django** | latest | тестирование |
| **flake8** | latest | проверка стиля кода |

---

## ⚙️ Установка и настройка

### 1️⃣ Клонировать репозиторий
```bash
git clone https://github.com/username/kurcovaya_5.git
cd kurcovaya_5
```

### 2️⃣ Установить зависимости
```bash
poetry install
```

### 3️⃣ Создать файл `.env` в корне проекта
```env
DEBUG=True
SECRET_KEY=dev-secret-key
DB_NAME=kurcovaya_5
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
TELEGRAM_TOKEN=your-telegram-bot-token
TELEGRAM_ADMIN_CHAT_ID=your-chat-id
```

### 4️⃣ Применить миграции
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Создать суперпользователя
```bash
python manage.py createsuperuser
```

### 6️⃣ Запустить Redis и Celery
Redis (Windows):
```bash
redis-server
```

Celery worker:
```bash
celery -A config worker -l info --pool=solo
```

Celery beat (для планировщика напоминаний):
```bash
celery -A config beat -l info
```

### 7️⃣ Запустить сервер Django
```bash
python manage.py runserver
```

После запуска проект будет доступен по адресу:  
👉 http://127.0.0.1:8000/

---

## 🔗 Основные эндпоинты API

| Метод | Эндпоинт | Описание |
|--------|-----------|-----------|
| `POST` | `/api/token/` | Авторизация (JWT) |
| `POST` | `/api/token/refresh/` | Обновление токена |
| `GET` | `/api/habits/habits/` | Список привычек текущего пользователя |
| `GET` | `/api/habits/habits/?public=true` | Список публичных привычек |
| `POST` | `/api/habits/habits/` | Создать привычку |
| `PUT` | `/api/habits/habits/{id}/` | Изменить привычку |
| `DELETE` | `/api/habits/habits/{id}/` | Удалить привычку |
| `GET` | `/api/users/me/` | Просмотр профиля пользователя |
| `GET` | `/api/docs/` | Swagger UI документация |

---

## 🤖 Telegram-интеграция

1. Создайте бота через [@BotFather](https://t.me/BotFather)
2. Получите токен и добавьте его в `.env`  
3. Получите свой `chat_id`, отправив любое сообщение боту и вызвав:
   ```
   https://api.telegram.org/bot<your_token>/getUpdates
   ```
4. Celery ежедневно отправляет напоминания о привычках в Telegram.

---

## 🧪 Тестирование

### Запуск тестов:
```bash
pytest
```

✅ Все тесты проходят успешно (5 тестов, 100% pass).  
Покрытие кода ≥ 80%.

---

## 🧹 Проверка кода
```bash
flake8 . --exclude=migrations
```
✅ 0 ошибок — код полностью соответствует PEP8.

---

## 🧰 Архитектура проекта

```
kurcovaya_5/
│
├── config/              # настройки Django и Celery
├── habits/              # приложение привычек
│   ├── models.py        # модель Habit
│   ├── views.py         # CRUD эндпоинты
│   ├── tasks.py         # Celery-задачи (напоминания)
│   ├── validators.py    # бизнес-правила
│   ├── permissions.py   # ограничения доступа
│   ├── tests/           # тесты API и моделей
│
├── telegram_bot/        # интеграция с Telegram API
│   ├── tasks.py
│   ├── services.py
│
├── users/               # пользователи и JWT
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│
├── pyproject.toml       # зависимости Poetry
├── .env.example         # пример конфигурации
├── README.md
```

---

## 📈 Результаты

| Критерий             | Статус |
|----------------------|--------|
| CORS                 | ✅     |
| Переменные окружения | ✅     |
| Модели и валидация   | ✅     |
| Эндпоинты            | ✅     |
| Права доступа        | ✅     |
| Telegram + Celery    | ✅     |
| Тесты ≥ 80%          | ✅     |
| Flake8 = 100%        | ✅     |
| Swagger              | ✅     |

---

> 🎓 *Проект выполнен в рамках курсовой работы по Django.*  
> Все требования ТЗ выполнены: Telegram-интеграция, Celery, Redis, JWT, CORS, тестирование и документация.
