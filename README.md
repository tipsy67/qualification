#qualification
Контекст Для быстрого масштабирования проекта применяется контейнеризация. Для этого вам предстоит «завернуть» ваш проект в Docker и настроить на самостоятельный запуск.

Для работы программы необходимо:

установленный docker
создать .env по примеру .env.example
sudo docker-compose up -d --build #команда для сборки и запука контейнеров
sudo docker-compose exec app python manage.py csu #команда для создания суперпользователя логин пользователя и пароль можно изменить в файле /users/management/commands/csu.py
загрузить при необходимости фикстуры sudo docker-compose exec app python manage.py loaddata ./data/fixtures/test_data_users.json sudo docker-compose exec app python manage.py loaddata ./data/fixtures/test_data_habits.json