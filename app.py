from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://darrenlackie@localhost:5432/setlist_app"
db = SQLAlchemy(app)
from models.gig import Gig
from models.song import Song
from models.setlist import Setlist

migrate = Migrate(app, db)
