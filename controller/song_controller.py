from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.song import Song
from models.setlist import Setlist
from models.gig import Gig
from app import db

songs_blueprint = Blueprint("songs", __name__)

songs_blueprint.route('/songs')
def all_songs():
    songs_returned = Song.query.all()
    return render_template('/songs/index.jinja', songs = songs_returned)

@songs_blueprint.route("/songs/<id>")
def show_song(id):
    selected_song = Song.query.get(id)
    selected_gigs = Gig.query.join(Setlist).filter(Setlist.song_id == id)
    return render_template("songs/show_song.jinja", song=selected_song, gigs=selected_gigs)
    