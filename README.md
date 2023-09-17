# YaCut ✂️

## Данный проект создан для того, чтобы сокращать длинные ссылки.

### Порядок установки:
1. Клонировать репозиторий и перейти в него в командной строке:

    ```
    git clone 
    ```

    ```
    cd yacut
    ```

2. Cоздать и активировать виртуальное окружение:

    ```
    python3 -m venv venv
    ```

    * Если у вас Linux/macOS
    
        ```
        source venv/bin/activate
        ```
    
    * Если у вас windows
    
        ```
        source venv/scripts/activate
        ```

3. Установить зависимости из файла requirements.txt:

    ```
    python3 -m pip install --upgrade pip
    ```
    
    ```
    pip install -r requirements.txt
    ```

4. Создать .env файл с таким содержанием:
   ```
   FLASK_APP = yacut
   FLASK_ENV = delelopment (или production)
   DATABASE_URI = sqlite:///db.sqlite3
   SECRET_KEY = <ваш секретный ключ>
   ```


### Использование:
1. ```flask run```

2. Доступен веб-сайт и API.
   - Для доступа к веб-сайту перейдите по адресу http://localhost:5000/
   - Для доступа в API отправляйте запросы на этот же адрес.

3. Схемы запросов к API:
   - http://localhost:5000/api/id/
     - POST: ``` {"url": "string", "custom_id": "string" * (необязательное поле)}``` - получить краткую ссылку из длинной ссылки (url), при желании можете предложить Ваш вариант короткой ссылки (custom_id).
   - http://localhost:5000/api/id/<short_id>/
     - GET - получить полную ссылку по <short_id>


<p align=center>
  <a href="url"><img src="https://github.com/xaer981/xaer981/blob/main/main_cat.gif" align="center" height="40" width="128"></a>
</p>
   
