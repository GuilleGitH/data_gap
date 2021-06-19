import json

def issue_form(self):
    return self.client.post(
        '/issue_form/',
        data=json.dumps(dict(
            date= '2021-03-16',
            time= '2021-03-16T21:28:47.932Z',
            plot= 0,
            issue_type= 0,
            description= 'string',
            note= 'string'
        )),
        content_type='application/json'
    )

def issue_form_field_based(self, field):
    return self.client.post(
        '/issue_form/field_based',
        data=json.dumps(dict(
            issue_form= dict(
                date= '2021-03-16',
                time= '2021-03-16T21:28:47.932Z',
                plot= 0,
                issue_type= 0,
                description= 'string',
                note= 'string'
            ),
            field_required= field
        )),
        content_type='application/json'
    )