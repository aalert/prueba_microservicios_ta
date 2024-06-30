import requests
from django import forms


class BaseForm():

    def send_request(self):
        method = self.cleaned_data['type']
        endpoint = self.cleaned_data['url']
        body = self.cleaned_data['body']

        url = f'http://service-3:8083/api/{endpoint}/'

        if method == 'GET':
            response = requests.get(url)
            return response.json()

        elif method == 'POST':
            headers = {'Content-Type': 'application/json'}
            response = requests.post(url, json=body, headers=headers)
            return response.json()


class ProcessForm(BaseForm, forms.Form):
    version = forms.ChoiceField(choices=[('1', '1'), ('2', '2')])
    timeSearch = forms.CharField()

class SearchForm(BaseForm, forms.Form):
    version = forms.ChoiceField(choices=[('1', '1'), ('2', '2')])
    alert_type = forms.ChoiceField(
        choices=[(None, "------"), ("ALTA", "ALTA"), ("MEDIA", "MEDIA"), ("BAJA", "BAJA")],
        required=False)
    sended = forms.NullBooleanField(required=False)

class SendForm(BaseForm, forms.Form):
    version = forms.ChoiceField(choices=[('1', '1'), ('2', '2')])
    alert_type = forms.ChoiceField(choices=[("ALTA", "ALTA"), ("MEDIA", "MEDIA"), ("BAJA", "BAJA")])


