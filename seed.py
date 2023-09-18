from app import db
from models.gig import Gig
from models.song import Song
from models.setlistitem import SetListItem
import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext
def seed():
    Gig.query.delete()
    Song.query.delete()

    song1 = Song(title="It's Thunder And It's Lightning", album="These Four Walls", running_time=5)
    song2 = Song(title="Quiet Little Voices", album="These Four Walls", running_time=5)
    song3 = Song(title="Repeating Patterns", album="The More I Sleep, The Less I Dream", running_time=4)
    gig1 = Gig(city="Edinburgh", venue="The Liquid Room", date="10-06-2023", set_time=75)
    gig2 = Gig(city="London", venue="Scala", date="12-06-2023", set_time=90)


    db.session.add(song1)
    db.session.add(song2)
    db.session.add(song3)

    db.session.add(gig1)
    db.session.add(gig2)

    db.session.commit()