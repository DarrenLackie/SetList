from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.setlist import Setlist
from models.gig import Gig
from models.song import Song

setlists_blueprint = Blueprint("setlists", __name__)