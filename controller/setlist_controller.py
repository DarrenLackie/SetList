from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.setlist import Setlist
from models.gig import Gig
from models.song import Song
from app import db

setlists_blueprint = Blueprint("setlists", __name__)

@setlists_blueprint.route('/setlists')
def all_setlists():
    setlists_returned = Setlist.query.all()
    # return render_template('/setlists/index.jinja', setlists = setlists_returned)
    return "Setlists page"
