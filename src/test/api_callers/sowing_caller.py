import json

def sowing_form(self):
    return self.client.post(
        '/sowing_form/',
        data=json.dumps(dict(
            date='2021-03-16',
            time='2021-03-16T19:21:33.196Z',
            plot=0,
            crop='string',
            quantity=0,
            time_to_harvest='string',
            harvest_duration='string',
            expected_yield='string',
            note='string'
        )),
        content_type='application/json'
    )

def sowing_form_field_based(self, field):
    return self.client.post(
        '/sowing_form/field_based',
        data=json.dumps(dict(
            sowing_form= dict(
                date='2021-03-16',
                time='2021-03-16T19:21:33.196Z',
                plot=0,
                crop='string',
                quantity=0,
                time_to_harvest='string',
                harvest_duration='string',
                expected_yield='string',
                note='string'
            ),
            field_required= field
        )),
        content_type='application/json'
    )