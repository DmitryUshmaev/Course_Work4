from marshmallow import Schema, fields

from setup_db import db

"""Модель director"""


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


"""Схема описания модели director"""


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
