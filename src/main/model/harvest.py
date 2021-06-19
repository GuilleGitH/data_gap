from .. import db, flask_bcrypt
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Harvest(db.Model):

    __tablename__ = 'harvest'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, nullable=False)
    plot_id = db.Column(db.Integer, ForeignKey('plot.id'))
    crop = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    harvest_quantity = db.Column(db.Integer, nullable=False)
