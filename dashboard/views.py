from django.shortcuts import render
from django.http import HttpResponse

import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required


@login_required
def index(request):

    response = requests.get(settings.API_URL)  # URL de la API
    users = response.json()  # Convertir la respuesta a JSON
    size = len(users)  # Convertir la respuesta a JSON

    data = {
        'title': "Landing Page' Dashboard",
        'responses': users,
        'size': size,
    }

    return render(request, 'dashboard/index.html', data)