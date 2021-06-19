from .. import db, flask_bcrypt
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Issue(db.Model):

    __tablename__ = 'issue'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    plot_id = db.Column(db.Integer, ForeignKey('plot.id'))
    issue_type = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return "<User '{}'>".format(self.name)
