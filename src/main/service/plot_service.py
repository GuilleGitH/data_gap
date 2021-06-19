import uuid
from datetime import datetime

from src.main import db
from src.main.model.plot import Plot


def new_plot(data):
    new_plot = Plot(
        name=data['name'],
        area=data['area'],
    )
    save_changes(new_plot)
    response_object = {
        'status': 'success',
        'message': 'Successfully registered a new Plot.'
    }
    return response_object, 201


def get_all():
    return Plot.query.all()


def get_by_id(public_id):
    return Plot.query.filter_by(id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
