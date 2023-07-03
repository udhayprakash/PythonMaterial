Step 1: Create virtual environment, and activate
python3 -m venv .myenv
source .myenv/bin/activate

Step 2: Install modules
pip install flask sphinx

Step 3: create docs folder and start sphnix

        cd docs
        sphinx-quickstart

Step 4: start flask app

        export FLASK_APP=app.py
        flask run
