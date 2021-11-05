from django.shortcuts import render
from django.http import HttpResponse, response
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import json
# Create your views here.
from apitest.models import Message

def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')

def get_all_msg(request, username):
    if request.method == "GET":
        try:
            lista = []
            last_ten = Message.objects.filter(username=username).order_by('msgId')[:]
            for obj in last_ten:
                ostatni_index = obj.msgId
            for i in range(ostatni_index+1):
                try:
                    msg = Message.objects.get(username=username, msgId=i)
                    odpowiedz = json.dumps({'Username' : username, 'Message': msg.message, "Id":msg.msgId})
                    lista.append(odpowiedz)
                except Message.DoesNotExist:
                    continue
            response = lista
        except:
            response = json.dumps([{'Error':'Brak wiadomosci od takiego usera'}])
        return HttpResponse(response,content_type='text/json')

def last_index_for_user(request,username):
    if request.method == "GET":
        try:
            lista = []
            last_ten = Message.objects.filter(username=username).order_by('msgId')[:]
            for obj in last_ten:
                ostatni_wpis = obj.message
            for obj in last_ten:
                ostatni_index = obj.msgId
            odpowiedz = json.dumps({'Username' : username,"Ostatnia wiadomosc":ostatni_wpis,"Ostatni index":ostatni_index})
            lista.append(odpowiedz)
            response = lista

        except:
            response = json.dumps([{'Error':'Brak wiadomosci od takiego usera'}])
        return HttpResponse(response,content_type='text/json')

@csrf_exempt
def add_msg(request):
    if request.method == "POST":
        payload = json.loads(request.body)
        username = payload['username']
        message = payload['message']
        car = Message(username=username, message = message)
        try:
            car.save()
            response = json.dumps([{'Success':'Message Sent correctly'}])
        except:
            response = json.dumps([{'Error': 'Could not send this message'}])

        return HttpResponse(response, content_type='text/json')