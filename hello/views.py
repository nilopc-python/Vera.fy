from django.shortcuts import render
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
        vars = dict()
        vars['output'] = truther.truthme(input_data)
        return render(request, 'input.html', context=vars, status=200)
        #return {
        #    "output": truther.truthme(input_data)
        #}
    else:
        return render(request, 'input.html')
    
    
