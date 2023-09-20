from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.setlistitem import SetListItem
from models.gig import Gig
from models.song import Song
from app import db

setlists_blueprint = Blueprint("setlists", __name__)

@setlists_blueprint.route('/setlists')
def all_setlists():
    setlists_returned = SetListItem.query.all()
    return render_template('/setlists/index.jinja', setlists = setlists_returned)

@setlists_blueprint.route("/setlists/new", methods=['GET'])
def new_setlist():
    songs = Song.query.all()
    gigs = Gig.query.all()
    return render_template("setlists/new.jinja", songs=songs, gigs=gigs)

@setlists_blueprint.route("/setlists",  methods=['POST'])
def add_to_setlist():
    song_ids = request.form.getlist('song_id')
    gig_id = request.form.get('gig_id')
    for song_id in song_ids:
        setlist = SetListItem(song_id=int(song_id), gig_id=gig_id)
        db.session.add(setlist)
    
    db.session.commit()
    return redirect('/setlists')

@setlists_blueprint.route("/setlists/<id>/delete", methods=['POST'])
def delete_song_from_setlist(id):
    set_list_item = SetListItem.query.get(id)
    gig_id = set_list_item.gig.id
    SetListItem.query.filter_by(id = id).delete()
    db.session.commit()
    return redirect(f'/gigs/{gig_id}')


