from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object("flask_blog.config")

db = SQLAlchemy(app)

from flask_blog.views import views, entries