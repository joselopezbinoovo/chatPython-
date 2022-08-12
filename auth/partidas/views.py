
from csv import reader
from email import message
from django.http.response import HttpResponse
from django.core import serializers
import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import partida, Juegos

class partidaView(View): 
    def get(self, request,): 
        partidas = partida.objects.select_related("juegoId").all()
        tmpJson = serializers.serialize("json",partidas)
        tmpObj = json.loads(tmpJson)
        return HttpResponse(json.dumps(tmpObj))
        #return JsHttpResponseonResponse(context, safe=False)   
        
# Create your views here.
