PY = venv/Scripts/python

migrate:
	$(PY) manage.py makemigrations
	$(PY) manage.py migrate

run:
	$(PY) manage.py runserver 8000
