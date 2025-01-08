### BF2 Qualification Daniil Toropov
Для работы программы необходимо:

1. установленный docker
2. создать .env по примеру .env.example
3. sudo docker-compose up -d --build #команда для сборки и запука контейнеров
4. sudo docker-compose exec app python manage.py csu #команда для создания суперпользователя логин пользователя и пароль можно изменить в файле /users/management/commands/csu.py
5. загрузить при необходимости фикстуры sudo docker-compose exec app python manage.py loaddata ./fixtures/all_data.json

### Описание задачи:

Необходимо создать сайт для компании медицинской диагностики. Сайт должен быть сверстан и подключен к админке. Для выполнения задачи необходимо использовать Django и Bootstrap. Сайт должен содержать основные разделы, необходимые для функционирования медицинской диагностической компании.

 

### Задача

1. Сверстать сайт для компании медицинской диагностики.
2. Подключить сайт к админке Django.
3. Использовать Bootstrap для создания адаптивного и привлекательного интерфейса.

 

### Функционал сайта:

1. **Главная страница**: 
   - Описание компании.
   - Перечень предоставляемых услуг.
   - Контактная информация.
   - Форма для обратной связи.
2. **Страница "О компании"**: 
   - История компании.
   - Миссия и ценности.
   - Команда врачей.
3. **Страница услуг**: 
   - Перечень предоставляемых медицинских услуг.
   - Подробное описание каждой услуги.
   - Цены на услуги.
4. **Страница "Контакты"**: 
   - Адрес компании.
   - Карта проезда.
   - Контактные телефоны и email.
   - Форма обратной связи.
5. **Личный кабинет**: 
   - Регистрация и авторизация пользователей.
   - Возможность записи на прием.
   - Просмотр истории записей и результатов диагностики.
6. **Админка**: 
   - Управление пользователями.
   - Управление услугами.
   - Управление записями на прием.
   - Управление контентом сайта (тексты, изображения и т.д.).

 

### Технические требования:

1. **Фреймворк**: 
   - Использовать фреймворк Django для реализации проекта.
2. **База данных**: 
   - Использовать PostgreSQL для хранения данных.
3. **Фронтенд**: 
   - Использовать Bootstrap для создания адаптивного интерфейса.
4. **Контейнеризация**: 
   - Использовать Docker и Docker compose для контейнеризации приложения.
5. **Документация**: 
   - В корне проекта должен быть файл README.md с описанием структуры проекта и инструкциями по установке и запуску.
6. **Качество кода**: 
   - Соблюдать стандарты PEP8.
   - Весь код должен храниться в удаленном Git репозитории.