import socket

import requests
from django.shortcuts import render

from rest_client.forms import ProcessForm, SearchForm, SendForm


def process(request):
    form = ProcessForm()

    context = {}

    if request.method == 'POST':
        form = ProcessForm(request.POST)
        if form.is_valid():
            body = {
                'version': int(form.cleaned_data['version']),
                'timeSearch': form.cleaned_data['timeSearch'],
            }

            response = call_api(body, 'process')
            context.update({
                'response': response,
            })

    context.update({
        'form': form,
    })

    return render(request, 'rest_client/process.html', context)


def search(request):
    form = SearchForm()

    context = {}

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            _type = form.cleaned_data.get('alert_type', None)
            if _type == "":
                _type = None
            body = {
                'version': form.cleaned_data['version'],
                'type': _type,
                'sended': form.cleaned_data.get('sended', None),
            }

            response = call_api(body, 'search')
            context.update({
                'response': response,
            })

    context.update({
        'form': form,
    })

    return render(request, 'rest_client/search.html', context)

def send(request):
    form = SendForm()

    context = {}

    if request.method == 'POST':
        form = SendForm(request.POST)
        if form.is_valid():
            body = {
                'version': form.cleaned_data['version'],
                'type': form.cleaned_data['alert_type'],
            }

            response = call_api(body, 'send')
            context.update({
                'response': response,
            })

    context.update({
        'form': form,
    })

    return render(request, 'rest_client/send.html', context)


def call_api(body, endpoint):
    url = f'http://servicio-3:8080/api/challenge/{endpoint}'

    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=body, headers=headers)

    return response.json