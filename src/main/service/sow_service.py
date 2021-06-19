import uuid
from datetime import datetime

from src.main import db
from src.main.model.sow import Sow
from src.main.model.plot import Plot


def save_new_sow(data):

    d, m, y = data['date'].split('/')
    sow_date = datetime(int(y), int(m), int(d))

    plot = Plot.get_a_plot(data['plot'].lower())

    new_sow = Sow(
        plot_id=plot.id,
        date=sow_date,
        crop=data['crop'],
        unit=data['unit'],
        quantity=data['quantity'],
        time_to_harvest=sow_date,
        harvest_duration=data['harvest_duration'],
        expected_yield=data['expected_yield']
    )
    save_changes(new_sow)
    response_object = {
        'status': 'success',
        'message': 'Successfully registered a new Sow.'
    }
    return response_object, 201


def get_all_sow():
    result = Sow.query.all()
    return result


def get_a_sow(public_id):
    return Sow.query.filter_by(public_id=public_id).first()


def get_join():
    result = db.session.query(Plot, Sow).join(Sow).all()
    return result


def save_changes(data):
    db.session.add(data)
    db.session.commit()
