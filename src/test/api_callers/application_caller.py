import json

def application_form(self):
    return self.client.post(
        '/application_form/',
        data=json.dumps(dict(
            date= '2021-03-16',
            time= '2021-03-16T21:31:27.302Z',
            plot= 0,
            product= 'string',
            quantity= 0,
            dose= 0,
            machine= 'string',
            note= 'string'
        )),
        content_type='application/json'
    )

def application_form_field_based(self, field):
    return self.client.post(
        '/application_form/field_based',
        data=json.dumps(dict(
            application_form= dict(
                date= '2021-03-16',
                time= '2021-03-16T21:31:27.302Z',
                plot= 0,
                product= 'string',
                quantity= 0,
                dose= 0,
                machine= 'string',
                note= 'string'
            ),
            field_required= field
        )),
        content_type='application/json'
    )