from app import db

class Gig(db.Model):
    __tablename__ = "gigs"

    id = db.Column(db.Integer, primary_key = True)
    city = db.Column(db.String(64))
    venue = db.Column(db.String(64))
    date = db.Column(db.String(10))
    set_time = db.Column(db.Integer)
    song_id = db.relationship("Song", backref="gig")

    def __repr__(self):
        return f"<Gig {self.id}: City {self.city}: Venue {self.venue}: Date {self.date}: Set Time {self.set_time}"