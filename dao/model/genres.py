from setup_db import db
from marshmallow import Schema, fields


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer)


class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
