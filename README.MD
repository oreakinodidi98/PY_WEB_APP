# python_OOP

## create a Virtual enviroment

- python -m venv venv
- activate the virtual enviroment: . .\venv\Scripts\Activate
- install dependencies
  - pip install django
  - python -m pip install Flask
  - pip install flake8
  - pip install waitress
  - pip install requests python-dotenv Flask
  - python -m pip install click
    - check code: flake8 <code>.py

- Deactivate the virtual environment: venv\Scripts\deactivate.bat
- or : deactivate

## generating a requirements file

- Here's how you can create a requirements.txt
- activate virtual nviroment: . .\venv\Scripts\Activate
- run command: pip freeze > requirements.txt
  - This command creates a requirements.txt file containing the names and versions of all installed packages
  - to include only the packages needed for your project (excluding development dependencies), you can use the:
  - pip freeze --exclude-editable > requirements.txt

## .gitignore file

- ignote
- .env
- .venv

## create folder structure

- static
  - styles
    - style.css
- templates
  - index.html
  - This is homepage everyone sees, can click "!" then TAB to get a skeleton
- main.py
- repository.py

in  index.html you can use

```html
<link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
or
<link href="{{ url_for('static', filename='styles/style.css') }}" rel="stylesheet" />
```

- can reference a CSS file with a <link> tag in the header of your HTML page

## enviroment variables

- enviroment variables
- import secrets
- secrets.token_hex()

## deploy to web

- go to [render.com](https://render.com/)
- connect github to acccount
- build command: pip install -U pip && pip install -r requirements.txt
  - to update pip and run requirements command
- start command: python3 main.py
- Advanced settings -> enviroment variable -> add API_key
  - also add PYTHON_VERSION
  - py -- version