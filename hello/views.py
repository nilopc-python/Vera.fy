from django.shortcuts import render
import sys
from django.http import HttpResponse
from .models import Greeting
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, Template

#from django.shortcuts import render_to_response
import logging
import truther
import webbrowser

@csrf_exempt
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def true(request):
    return render(request, 'inputT.html')

@csrf_exempt
def false(request):
    return render(request, 'inputF.html')

@csrf_exempt
def inputt(request):
    if request.method == 'POST':
        input_data = request.POST.get("input_str")
        output = HttpResponse(truther.truthme(input_data))

        if truther.truthme(input_data):
            return render(request, 'inputT.html')
        else:
            return render(request, 'inputF.html')
        
        #return render(request, 'input.html', context=vars)
        #return {
        #    "output": str(truther.truthme(input_data))
        #}
    else:
        return render(request, 'input.txt')
