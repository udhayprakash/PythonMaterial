# pip install gunicorn fcntl
from app import app

if __name__ == "__main__":
    app.run()


# gunicorn wsgi:app -c gunicorn.conf.py
