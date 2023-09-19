from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://darrenlackie@localhost:5432/setlist_app"
db = SQLAlchemy(app)
from models.gig import Gig
from models.song import Song
from models.setlistitem import SetListItem

migrate = Migrate(app, db)

from seed import seed
app.cli.add_command(seed)

from controllers.gig_controller import gigs_blueprint
from controllers.song_controller import songs_blueprint
from controllers.setlist_controller import setlists_blueprint

app.register_blueprint(gigs_blueprint)
app.register_blueprint(songs_blueprint)
app.register_blueprint(setlists_blueprint)

@app.route('/')
def home():
    return render_template('index.jinja')

if __name__ == '__main__':
    app.run(debug=True)
