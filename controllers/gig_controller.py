from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gig import Gig
from models.setlistitem import SetListItem
from models.song import Song
from app import db

gigs_blueprint = Blueprint("gigs", __name__)

@gigs_blueprint.route('/gigs')
def all_gigs():
    returned_gigs = Gig.query.all()
    return render_template('/gigs/index.jinja', gigs=returned_gigs)

@gigs_blueprint.route("/gigs/<id>")
def show_gig(id):
    selected_gig = Gig.query.get(id)
    songs = Song.query.all()
    return render_template("gigs/show_gig.jinja", gig=selected_gig, songs=songs)

@gigs_blueprint.route("/gigs", methods=["POST"])
def add_new_gig():
    gig_date = request.form["date"]
    gig_city = request.form["city"]
    gig_venue = request.form["venue"]
    gig_set_time = request.form["set_time"]

    gig_to_be_saved = Gig(date=gig_date, city=gig_city, venue=gig_venue, set_time=gig_set_time)
    db.session.add(gig_to_be_saved)
    db.session.commit()
    return redirect ("/gigs")

@gigs_blueprint.route("/gigs/<id>/delete", methods=['POST'])
def delete_gig(id):
    Gig.query.filter_by(id = id).delete()
    db.session.commit()
    return redirect('/gigs')

@gigs_blueprint.route("/gigs/<id>/setlists/new", methods=['POST'])
def create_setlist_in_gig(id):
    song_ids = request.form.getlist('song_id[]')
    gig_id = id
    for song_id in song_ids:
        setlist = SetListItem(song_id=int(song_id), gig_id=gig_id)
        db.session.add(setlist)
    
    db.session.commit()
    return redirect(f'/gigs/{gig_id}')

@gigs_blueprint.route("/gigs/<id>/update")
def show_update_gig_page(id):
    gig_to_update = Gig.query.get(id)
    return render_template("gigs/update.jinja", gig=gig_to_update)


@gigs_blueprint.route("/gigs/<id>/update", methods=["POST"])
def update_gig(id):
    gig_to_update = Gig.query.get(id)

    new_gig_city = request.form["city"]
    new_gig_venue = request.form["venue"]
    new_gig_date = request.form["date"]
    new_gig_set_time = request.form["set_time"]

    gig_to_update.city = new_gig_city
    gig_to_update.venue = new_gig_venue
    gig_to_update.date = new_gig_date
    gig_to_update.set_time = new_gig_set_time

    db.session.commit()

    return redirect(f'/gigs/{gig_to_update.id}')
