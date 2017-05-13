init:
    pip install pipenv
    pipenv lock
    pipenv install

test:
    pipenv run manage.py test