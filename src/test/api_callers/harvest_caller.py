import json

def harvest_form(self):
    return self.client.post(
        '/harvesting_form/',
        data=json.dumps(dict(
            date= '2021-03-16',
            time= '2021-03-16T21:23:10.985Z',
            plot= 0,
            quantity= 0,
            harvest_quantity= 'string',
            note= 'string'
        )),
        content_type='application/json'
    )

def harvest_form_field_based(self, field):
    return self.client.post(
        '/harvesting_form/field_based',
        data=json.dumps(dict(
            harvesting_form= dict(
                date= '2021-03-16',
                time= '2021-03-16T21:23:10.985Z',
                plot= 0,
                quantity= 0,
                harvest_quantity= 'string',
                note= 'string'
            ),
            field_required= field
        )),
        content_type='application/json'
    )