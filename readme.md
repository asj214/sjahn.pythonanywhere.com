# sjahn.pythonanywhere.com for flutter apps


1. python venv  
    ```shell
    python3 -m venv .venv
    . .venv/bin/activate
    python3 -m pip install --upgrade pip
    ```
2. `pip3 install -r requirements.txt`  
3. `cp .env.example .env`  
4. database migrate  
    ```shell
    python3 db.py migrate
    ```
5. `FLASK_DEBUG=1 flask run`  



swagger:  ''
