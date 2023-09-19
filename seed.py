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
    song4 = Song(title="Moving Clocks Run Slow", album="These Four Walls", running_time=5)
    song5 = Song(title="Ships With Holes Will Sink", album="These Four Walls", running_time=4)
    song6 = Song(title="Roll Up Your Sleeves", album="These Four Walls", running_time=5)
    song7 = Song(title="Conductor", album="These Four Walls", running_time=5)
    song8 = Song(title="Keeping Warm", album="These Four Walls", running_time=8)
    song9 = Song(title="Short Bursts", album="These Four Walls", running_time=6)
    song10 = Song(title="Human Error", album="In The Pit Of The Stomach", running_time=4)
    
    gig1 = Gig(city="Edinburgh", venue="The Liquid Room", date="10-06-2023", set_time=75)
    gig2 = Gig(city="London", venue="Scala", date="12-06-2023", set_time=90)


    db.session.add(song1)
    db.session.add(song2)
    db.session.add(song3)
    db.session.add(song4)
    db.session.add(song5)
    db.session.add(song6)
    db.session.add(song7)
    db.session.add(song8)
    db.session.add(song9)
    db.session.add(song10)

    db.session.add(gig1)
    db.session.add(gig2)

    db.session.commit()