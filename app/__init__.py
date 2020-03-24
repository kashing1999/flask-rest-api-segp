from flask import Flask
from flask import jsonify, abort, request
from flask_jwt import JWT
from app.database import __init_db

# import torchvision.transforms as transforms
# from PIL import Image

from config import Config
app = Flask(__name__)
app.config.from_object(Config)

# DB
__init_db(app)

# JWT
from app.auth import authenticate, identity

jwt = JWT(app, authenticate, identity)

# Rubbish Recognition
from app import inference
inference = inference.Inference('./weights.pth')

from app import routes, models
