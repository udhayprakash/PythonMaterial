virtualenv venv
venv/Scripts/activate.bat
pip install flask flask-jsonpify flask-sqlalchemy flask-restful
pip freeze > requirements.txt