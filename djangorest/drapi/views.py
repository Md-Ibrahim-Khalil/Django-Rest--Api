from django.shortcuts import render
from . models import Aiquest
from .serializers import AiquestSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
#Queryset
def aiquest_info(request):
    #complex data
    ai = Aiquest.objects.all()
    #python dict
    serializer = AiquestSerializer(ai, many=True)
    json_data = JSONRenderer().render(serializer.data)
    #json sent to user
    return HttpResponse(json_data, content_type='application/json')

#Model Instance
def aiquest_ins(request, pk):
    #complex data
    ai = Aiquest.objects.get(id=pk)
    #python dict
    serializer = AiquestSerializer(ai)
    json_data = JSONRenderer().render(serializer.data)
    #json sent to user
    return HttpResponse(json_data, content_type='application/json')