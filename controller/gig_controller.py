from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gig import Gig
from models.setlist import Setlist
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

# @gigs_blueprint.route("/gigs/<id>/delete", methods=['POST'])
# def delete_song_from_setlist(id):
#     Gig.query.filter_by(id = id).delete()
#     db.session.commit()
#     return redirect(f'/gigs')