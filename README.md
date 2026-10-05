# Barber Jaster — Django сайт барбершопу

У проєкті є:

- головна сторінка;
- реєстрація користувача;
- вхід / вихід;
- запис на прийом;
- вибір послуги, дати і часу;
- сторінка "Мої записи";
- можливість скасувати запис;
- Django Admin;
- HTML + CSS + JavaScript;
- SQLite база даних.

## Запуск на Windows 11

Відкрий папку проєкту у VS Code і в Terminal виконай:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Після цього відкрий:

```text
http://127.0.0.1:8000/
```

## Створити адміністратора

```bash
python manage.py createsuperuser
```

Адмінка:

```text
http://127.0.0.1:8000/admin/
```

## Де що знаходиться

- `main/templates/main/home.html` — головна
- `main/templates/main/register.html` — реєстрація
- `main/templates/main/login.html` — вхід
- `main/templates/main/booking.html` — запис на прийом
- `main/templates/main/my_bookings.html` — мої записи
- `main/static/main/css/style.css` — CSS
- `main/static/main/js/script.js` — JavaScript
- `main/models.py` — модель запису
- `main/forms.py` — форми
- `main/views.py` — логіка Django
