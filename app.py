from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://darrenlackie@localhost:5432/setlist_app"
db = SQLAlchemy(app)
from models.gig import Gig
from models.song import Song
from models.setlist import Setlist

migrate = Migrate(app, db)

from seed import seed
app.cli.add_command(seed)

from controller.gig_controller import gigs_blueprint
from controller.song_controller import songs_blueprint
from controller.setlist_controller import setlists_blueprint

app.register_blueprint(gigs_blueprint)
app.register_blueprint(songs_blueprint)
app.register_blueprint(setlists_blueprint)

@app.route('/')
def home():
    return render_template('index.jinja')

if __name__ == '__main__':
    app.run(debug=True)
