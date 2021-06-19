from .. import db, flask_bcrypt
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Application(db.Model):

    __tablename__ = 'application'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, nullable=False)
    plot_id = db.Column(db.Integer, ForeignKey('plot.id'))
    product = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    dose = db.Column(db.Float, nullable=False)
    machine = db.Column(db.String(255), nullable=False)
