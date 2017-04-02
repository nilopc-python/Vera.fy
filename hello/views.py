from django.shortcuts import render
import sys
from django.http import HttpResponse
from .models import Greeting
from django.views.decorators.csrf import csrf_exempt
#from django.shortcuts import render_to_response
import truther
import webbrowser

@csrf_exempt
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def inputt(request):
    if request.method == 'POST':
        input_data = request.POST.get("input_str")

        if truther.truthme(input_data):
            webbrowser.open_new("http://google.com")
        else:
            webbrowser.open_new("http://bing.com")
            
        return render(request, 'input.html')
        #return {
        #    "output": str(truther.truthme(input_data))
        #}
    else:
        return render(request, 'input.html')
    
    
