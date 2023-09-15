from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gig import Gig
from models.setlist import Setlist
from models.song import Song

gigs_blueprint = Blueprint("gigs", __name__)

