# TODO:
- Session logins (Flaks-JWT)
- Passwords (done, not tested)

# How to run
- Run `pipenv shell` to start a virtual env
- Run `pipenv install` to install dependencies
- Download the pretrained [weights](https://drive.google.com/open?id=16fTx2CFWCI82DWMBfqK7Oszuc1dK3KzZ) and place it in the project root directory
- Migrate db with `flask db migrate`
- Apply changes to db with `flask db upgrade`
- Run with `python3 rest-api.py`

# Adapted from
1. https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
2. https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
3. https://pythonhosted.org/Flask-JWT/
