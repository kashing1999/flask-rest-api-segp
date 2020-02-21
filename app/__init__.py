from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import jsonify, abort, request

# import torchvision.transforms as transforms
# from PIL import Image

from config import Config
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import inference

inference = inference.Inference('./weights.pth')

from app import routes, models, db