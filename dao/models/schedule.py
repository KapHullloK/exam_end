from setup_db import db
from marshmallow import Schema, fields


class Schedule(db.Model):
    __tablename__ = 'schedule'

    id = db.Column(db.Integer, primary_key=True)
    school_subject = db.Column(db.String(50))
    date_subject = db.Column(db.String(25))
    fio = db.Column(db.String(100))
    office = db.Column(db.Integer())


class ScheduleSchema(Schema):
    id = fields.Int(dump_only=True)
    school_subject = fields.Str()
    date_subject = fields.Str()
    fio = fields.Str()
    office = fields.Int()
