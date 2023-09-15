from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.song import Song
from models.setlist import Setlist
from models.gig import Gig

songs_blueprint = Blueprint("songs", __name__)


