##########################
# example of extracting logic/verbosity
##########################



def update_song_obj(song_to_update, request_form):
    new_song_title = request_form["title"]
    new_song_album = request_form["album"]
    new_song_running_time = request_form["running_time"]

    song_to_update.title = new_song_title
    song_to_update.album = new_song_album
    song_to_update.running_time = new_song_running_time

