# === Stage 1: Base Python image ===
FROM python:3.13-slim

# === Install system dependencies ===
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && apt-get clean

# === Set working directory ===
WORKDIR /app

# === Copy dependency files ===
COPY pyproject.toml poetry.lock* ./

# === Install Poetry manually ===
RUN pip install --upgrade pip \
    && pip install poetry

# === Configure Poetry ===
RUN poetry config virtualenvs.create false

# === Install dependencies ===
# Важно: без "--no-dev"
RUN poetry install --no-interaction --no-ansi

# === Copy the rest of the project ===
COPY . .

# === Collect static files (ignore errors if no static) ===
RUN mkdir -p /app/static && python manage.py collectstatic --noinput || true

# === Expose Django port ===
EXPOSE 8000

# === Default command ===
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
