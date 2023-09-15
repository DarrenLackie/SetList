from app import db

class Song(db.Model):
    id = db.Column(db.Integer)
    title = db.Column(db.String(255))
    album = db.Column(db.String(255))
    running_time = db.Column(db.Integer)
    gig_id = db.relationship("Gig", backref="song")

    def __repr__(self):
        return f"<Song {self.id}: Title {self.title}: Album {self.album}: Song Length {self.running_time}>"