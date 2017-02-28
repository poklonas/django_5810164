from django.shortcuts import render
from django.apps import apps

def homepage(request):
    # test try to get app name 
    s = apps.get_models()
    print(s)
    # ## #
    return render(request, 'homepage/index.html')
