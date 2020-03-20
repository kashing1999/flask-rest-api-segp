from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = None
migrate = None
def __init_db(app):
    global db
    global migrate
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    return (db, migrate)