from .. import db, flask_bcrypt
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .plot import Plot

Base = declarative_base()


class Sow(db.Model):

    __tablename__ = 'sow'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, nullable=False)
    plot_id = db.Column(db.Integer, ForeignKey('plot.id'))
    crop = db.Column(db.String(255), nullable=False)
    unit = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    time_to_harvest = db.Column(db.DateTime, nullable=False)
    harvest_duration = db.Column(db.Integer, nullable=False)
    expected_yield = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Sow '{}'>".format(self.crop)

    def serialize(self):
        serialized_instance = {}
        serialized_instance["id"] = self.id
        serialized_instance["date"] = self.date
        serialized_instance["plot_id"] = self.plot_id
        serialized_instance["crop"] = self.crop
        serialized_instance["unit"] = self.unit
        serialized_instance["quantity"] = self.quantity
        serialized_instance["time_to_harvest"] = self.time_to_harvest
        serialized_instance["harvest_duration"] = self.harvest_duration
        serialized_instance["expected_yield"] = self.expected_yield
        return serialized_instance
