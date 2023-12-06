from setup_db import db
from sqlalchemy.orm import relationship


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.String)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    genre = relationship('Genre')
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    director = relationship('Director')

