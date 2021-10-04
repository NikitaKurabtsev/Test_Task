# Test_Task

1. pipenv shell
2. pipenv run python manage.py runserver
3. docker-compose up
4. celery -A test_task beat
5. celery -A test_task worker -l INFO --pool=solo