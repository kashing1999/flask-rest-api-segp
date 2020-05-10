# How to run
- Install pip
- Run `pipenv shell` to start a virtual env
- Run `pipenv install` to install dependencies
- Download the pretrained [weights](https://drive.google.com/open?id=16fTx2CFWCI82DWMBfqK7Oszuc1dK3KzZ) and place it in the project root directory
- Migrate db with `flask db migrate`
- Apply changes to db with `flask db upgrade`
- Run locally with `python3 rest-api.py`
- Or use gunicorn: `gunicorn -b 0.0.0.0:8000 -w 1 rest-api:app`
