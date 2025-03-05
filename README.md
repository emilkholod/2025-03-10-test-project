# Проект: fastapi-postgresql-version

## Описание
Тестовый проект на fastapi, который имеет единственный API: возвращает текущую версию базы данных.

## Требования
Перед запуском убедитесь, что на вашем компьютере установлены:
- Docker
- Docker Compose

## Установка
1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/emilkholod/fastapi-postgresql-version.git
   cd fastapi-postgresql-version
   ```
2. Соберите контейнеры:
   ```sh
   make build
   ```
3. Запустите приложение:
   ```sh
   make up
   ```

## Использование
- Для остановки сервисов:
  ```sh
  make down
  ```
- Для запуска тестов выполните команду:
  ```sh
  make test
  ```
- Для создания production образа:
  ```sh
  make prod
  ```
- Для открытия shell внутри контейнера:
  ```sh
  make sh
  ```

## Структура проекта
- `src/` — исходный код проекта
- `tests/` — тесты
- `Dockerfile` — конфигурация Docker-образа
- `docker-compose.yml` — настройка сервисов для разработки
- `Makefile` — автоматизация команд
