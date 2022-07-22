migrations: python manage.py migrate
web: uvicorn bvc.asgi:application --host=0.0.0.0 --port=${PORT:-8000} --workers=4
