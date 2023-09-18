from app import db

class SetListItem(db.Model):
    __tablename__ = "setlists"

    id = db.Column(db.Integer, primary_key = True) 
    gig_id = db.Column(db.Integer, db.ForeignKey('gigs.id'))
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'))

    def __repr__(self):
        return f"<Set List {self.id}>"