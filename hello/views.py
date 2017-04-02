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
        t = Template('''
{% load static %} 

<!DOCTYPE html>
<html>

  <head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>Vera.fy</title>
    <link href='https://fonts.googleapis.com/css?family=Source+Sans+Pro' rel='stylesheet'>

    <link rel='stylesheet' type='text/css' href= '{% static 'style.css' %}'/>

  </head>

  <body align='center'>

    <div style='padding: 50px'>
      <form id='myForm'>
        <h2> What do you want to know? </h2>
        <p>
          <input type='text' name='input_str' id='myInput'><button id='myButton' type='submit'>Fact check!</button>
        </p>
    </form>
  </div>
    <!-- save space for truth value output -->

          <div id='infoLabel' style='padding: 20px'>{{ message|default_if_none:'DNE'}}</div>
  </body>

</html>
        ''')

        if truther.truthme(input_data):
            c = Context({'message': 'True'})
            html = t.render(c)
            return render(request, 'index.html')
        else:
            c = Context({'message': 'False'})
            html = t.render(c)
            return render(request, 'index.html')

        #return render(request, 'input.html', context=vars)
        #return {
        #    "output": str(truther.truthme(input_data))
        #}
    else:
        return render(request, 'index.html')
