# 🧠 Habit Tracker — Сервис привычек с напоминаниями и Telegram-интеграцией
**Habit Tracker** — это Django REST API-сервис для создания, отслеживания и напоминания о полезных и приятных привычках.  
Приложение полностью контейнеризировано с помощью **Docker Compose**, поддерживает **CI/CD через GitHub Actions**, и
автоматически деплоится на удалённый сервер.

🔗 **Деплой:** [http://158.160.52.224](http://158.160.52.224)

---

## 🚀 Основные возможности
- ✅ CRUD-операции с привычками  
- 🔔 Напоминания в **Telegram**  
- 🔁 Периодичность выполнения (по умолчанию ежедневно)  
- 💬 Разделение на полезные и приятные привычки  
- 🔒 Авторизация по **JWT-токенам**  
- 🌐 Поддержка **CORS** для фронтенда  
- 📄 Swagger / OpenAPI-документация  
- ⚙️ Асинхронные задачи через **Celery + Redis**  
- 🧩 Контейнеризация (Django, PostgreSQL, Redis, Celery, Nginx)  
- 🚀 Автоматический деплой через **GitHub Actions**

---

## 🏗️ Технологический стек
| Компонент                 | Версия  | Назначение                  |
|---------------------------|---------|-----------------------------|
| **Python**                | 3.13    | язык разработки             |
| **Django**                | 6.0.1   | веб-фреймворк               |
| **Django REST Framework** | latest  | REST API                    |
| **PostgreSQL**            | 17      | основная база данных        |
| **Redis**                 | 7       | брокер сообщений Celery     |
| **Celery**                | 5.6.2   | планировщик задач           |
| **Nginx**                 | latest  | обратный прокси             |
| **Docker Compose**        | 3.9     | управление контейнерами     |
| **GitHub Actions**        | latest  | CI/CD пайплайн              |
| **pytest / flake8**       | latest  | тестирование и линтинг кода |

---

## ⚙️ Установка и запуск проекта локально
### 1️⃣ Клонирование репозитория

git clone https://github.com/username/kurcovaya_5.git
cd kurcovaya_5

### 2️⃣ Создание файла окружения .env

Используй шаблон .env.example:

DEBUG=True
SECRET_KEY=dev-secret-key

DB_NAME=kurcovaya_5
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=db
DB_PORT=5432

CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0

TELEGRAM_TOKEN=your_telegram_token
TELEGRAM_ADMIN_CHAT_ID=your_chat_id

ALLOWED_HOSTS=127.0.0.1,localhost

### 3️⃣ Запуск всех контейнеров
docker compose up -d --build

После запуска:
Django будет доступен на http://localhost:8000
Nginx проксирует запросы на http://localhost

## 📦 Структура контейнеров

| Сервис     | Образ            | Порт | Назначение              |
| ---------- | ---------------- | ---- | ----------------------- |
| **web**    | python:3.13-slim | 8000 | Django + Gunicorn       |
| **db**     | postgres:17      | 5432 | база данных             |
| **redis**  | redis:7          | 6379 | брокер Celery           |
| **celery** | custom           | —    | обработка фоновых задач |
| **beat**   | custom           | —    | планировщик задач       |
| **nginx**  | nginx:latest     | 80   | прокси-сервер           |

## 🌐 CI/CD с GitHub Actions

Workflow-файл: .github/workflows/deploy.yml
Что делает пайплайн:
Проверяет код с помощью flake8
Запускает pytest
Собирает Docker-образы
Подключается к серверу по SSH
Выполняет:

cd ~/kurcovaya_5
git pull origin vetka_2_course_8
docker compose down
docker compose build --no-cache
docker compose up -d

Настройка GitHub Secrets:
Переменная	Значение
SERVER_IP	158.160.52.224
SERVER_USER	ubuntu
SERVER_SSH_KEY	приватный ключ id_ed25519_github_actions
## 🧾 API эндпоинты
Метод	Эндпоинт	Описание
POST	/api/token/	Авторизация (JWT)
POST	/api/token/refresh/	Обновление токена
GET	/api/habits/habits/	Список привычек пользователя
GET	/api/habits/habits/?public=true	Публичные привычки
POST	/api/habits/habits/	Создать привычку
PUT	/api/habits/habits/{id}/	Изменить привычку
DELETE	/api/habits/habits/{id}/	Удалить привычку
GET	/api/users/me/	Профиль пользователя
GET	/api/docs/	Swagger UI
## 🤖 Telegram-интеграция

Создайте бота через @BotFather
Добавьте токен в .env
Получите chat_id:
https://api.telegram.org/bot<your_token>/getUpdates


Celery ежедневно отправляет напоминания пользователям в Telegram.

## 🧪 Тестирование и линтинг
Запуск тестов:
pytest

Проверка стиля кода:
flake8 . --exclude=migrations


✅ 100% PEP8
✅ Все тесты проходят успешно

## 📂 Архитектура проекта
kurcovaya_5/
│
├── config/              # настройки Django и Celery
├── habits/              # логика привычек
│   ├── models.py
│   ├── tasks.py
│   ├── validators.py
│   ├── tests/
│
├── telegram_bot/        # Telegram-интеграция
│   ├── services.py
│   ├── tasks.py
│
├── users/               # пользователи и JWT
│   ├── serializers.py
│   ├── views.py
│
├── docker-compose.yml   # контейнеры проекта
├── Dockerfile           # сборка образа Django
├── nginx.conf           # конфигурация Nginx
├── .env.example         # пример переменных окружения
├── .github/workflows/   # CI/CD пайплайн
└── README.md

## 📈 Результаты
Критерий	                  Статус
Docker-контейнеризация	        ✅
PostgreSQL + Redis            	✅
Celery + Beat	                ✅
Nginx-прокси	                ✅
CI/CD через GitHub Actions	    ✅
SSH-деплой	                    ✅
Автоматический билд и рестарт	✅
Документация и API Swagger	    ✅
PEP8 / flake8 / pytest	        ✅
Всё доступно на сервере	        ✅

```bash