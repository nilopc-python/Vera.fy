from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting
from django.views.decorators.csrf import csrf_exempt

import truther

@csrf_exempt
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def inputt(request):
    if request.POST:
        input_data = request.POST.get("input_str")
        return HttpResponse(truther.truthme(input_data), status=200)
    else:
        return render(request, 'input.html')
    
    
