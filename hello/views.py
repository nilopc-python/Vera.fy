from django.shortcuts import render
import sys
from django.http import HttpResponse
from .models import Greeting
from django.views.decorators.csrf import csrf_exempt
#from django.shortcuts import render_to_response
import truther

@csrf_exempt
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def inputt(request):
    if request.method == 'POST':
        input_data = request.POST.get("input_str")
        #vars = dict()
        temp_var = "False"
        if truther.truthme(input_data):
            temp_var = "True"
            #vars['output'] = "True"
        #else:
        #    vars['output'] = "False"
        print >>sys.stderr, temp_var
        return {
            "output": str(truther.truthme(input_data))
        }
        #return render(request, 'input.html', context=vars, status=200)
        return {
            "output": str(truther.truthme(input_data))
        }
    else:
        return render(request, 'input.html')
    
    
