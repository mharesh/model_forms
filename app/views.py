from django.http import HttpResponse
from django.shortcuts import render
from app.forms import *

# Create your views here.
def insert_topic(request):
    ETFO =TopicForm()
    d={'ETFO':ETFO}
    if request.method == 'POST':
        DTFO = TopicForm(request.POST)
        if DTFO.is_valid():
            DTFO.save()
            return HttpResponse('Topic Data is Created ')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WFEO = WebpageForm()
    m={'WFEO':WFEO}
    if request.method == 'POST':
        WFDO = WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('DATA collected')

    return render(render,'insert_webpage.html',m)