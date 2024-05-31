from flask import Flask
# from flask_cors import CORS

app = Flask(__name__)
"""
app = Flask(__name__, static_folder="./build/static", template_folder="./build")
CORS(app) #Cross Origin Resource Sharing
"""

app.config.from_object("salary.config")
import salary.views