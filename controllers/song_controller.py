from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.song import Song
from models.setlistitem import SetListItem
from models.gig import Gig
from app import db

songs_blueprint = Blueprint("songs", __name__)

@songs_blueprint.route('/songs')
def all_songs():
    songs_returned = Song.query.all()
    return render_template('/songs/index.jinja', songs = songs_returned)

@songs_blueprint.route("/songs/<id>")
def show_song(id):
    selected_song = Song.query.get(id)
    # selected_gigs = Gig.query.join(SetListItem).filter(SetListItem.song_id == id)
    return render_template("songs/show_song.jinja", song=selected_song)

@songs_blueprint.route('/songs', methods=["POST"])
def add_new_song():
    song_name = request.form["title"]
    song_album = request.form["album"]
    song_run_time = request.form["run_time"]

    song_to_add = Song(title=song_name, album=song_album, running_time=song_run_time)
    db.session.add(song_to_add)
    db.session.commit()
    return redirect('/songs')

@songs_blueprint.route("/songs/<id>/delete", methods=['POST'])
def delete_song(id):
    Song.query.filter_by(id = id).delete()
    db.session.commit()
    return redirect(f'/songs')

@songs_blueprint.route("/songs/<id>/update")
def show_update_song_page(id):
    song_to_update = Song.query.get(id)
    return render_template("songs/update.jinja", song=song_to_update)

@songs_blueprint.route("/songs/<id>/update", methods=["POST"])
def update_song(id):
    song_to_update = Song.query.get(id)

    new_song_title = request.form["title"]
    new_song_album = request.form["album"]
    new_song_running_time = request.form["running_time"]

    song_to_update.title = new_song_title
    song_to_update.album = new_song_album
    song_to_update.running_time = new_song_running_time

    db.session.commit()

    return redirect(f'/songs/{song_to_update.id}')

