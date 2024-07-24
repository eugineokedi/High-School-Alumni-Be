from flask import Flask
from dotenv import load_dotenv
load_dotenv()
import os
from flask_restful import Api,Resource
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_cors import CORS


app = Flask(__name__)
app.secret_key = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///munchinkenya.db" 
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.init_app(app)


bcrypt = Bcrypt(app)
api = Api(app)
CORS(app)



