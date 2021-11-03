from django.shortcuts import render
from django.http import HttpResponse, response
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import json
# Create your views here.
from myapp.models import Message

def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')

def get_car(request, username):
    if request.method == "GET":
        try:
            lista = [{'Wiadomości od: ' : username}]
            for i in range(10):
                try:
                    msg = Message.objects.get(username=username, msg_id = i)
                    odpowiedz = json.dumps({'Username' : username, 'MessageId: ': msg.msg_id, 'Message': msg.message})
                    lista.append(odpowiedz)
                except Message.DoesNotExist:
                    continue

            response = lista

        except:
            response = json.dumps([{'Error':'Brak wiadomosci od takiego usera'}])
        return HttpResponse(response,content_type='text/json')

@csrf_exempt
def add_car(request):
    if request.method == "POST":
        payload = json.loads(request.body)
        username = payload['username']
        msg_id = payload['msg_id']
        message = payload['message']
        car = Message(username=username, msg_id=msg_id, message = message)
        try:
            car.save()
            response = json.dumps([{'Success':'Message Sent correctly'}])
        except:
            response = json.dumps([{'Error': 'Could not send this message'}])

        return HttpResponse(response, content_type='text/json')