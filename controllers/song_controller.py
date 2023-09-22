from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.song import Song
from models.setlistitem import SetListItem
from models.gig import Gig
from services.song_services import update_song_obj
from app import db


# we can consider extracting out logic and extra verbosity from our controller functions, we care more about _what_ are code is doing as opposed to _how_ its doing it. 
# see below for example
# this has the following benefits ..

# 1. Separation of concerns
# One of the core principles of software engineering is the separation of concerns. By moving business logic out of controllers and into separate components, you ensure that each component has a single responsibility. Controllers should primarily handle user input and orchestrate the flow of data, while logic related to data manipulation, validation, and business rules should be handled by other parts of the application.
# 2. Code Reusability (keeps us DRY)
# Extracting logic into separate modules or classes makes it more reusable. You can use the same logic in multiple controllers or even in different parts of your application. This reduces code duplication and leads to a more maintainable codebase.
# 3. Scalable 
# As your application grows, you may need to change or extend its functionality, if we have to do the same action several times, it helps if we have the logic to do that action central to one place if we suddenly need to change how we are doing that action we now need to just change the code in one place as apposed to every place we where doing that action.
# 4. Readability 
# Controllers are typically responsible for managing the flow of requests and responses. When logic is mixed with controller code, it can make controllers bulky and less readable. Extracting logic into separate files/folders leads to cleaner, more focused, and more readable code. This improves the overall maintainability of the application. 



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

 
##########################
# example of extracting logic/verbosity
##########################
# @songs_blueprint.route("/songs/<id>/update", methods=["POST"])
# def update_song(id):
#     song_to_update = Song.query.get(id)
#     update_song_obj(song_to_update, request.form)

#     db.session.commit()

#     return redirect(f'/songs/{song_to_update.id}')

 