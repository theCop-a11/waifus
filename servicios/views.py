from django.shortcuts import render

from servicios.models import Servicio

# Create your views here.

def servicios(request):

    servicios = Servicio.objects.all() # pylint: disable=maybe-no-member
    return render(request, "servicios/servicios.html", {"servicios": servicios})

