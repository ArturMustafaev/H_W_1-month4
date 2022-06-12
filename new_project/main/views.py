from django.shortcuts import render

# Create your views here.

def index(request):
    dict_={
        'key': "Hello World",
        'color': '#05fc89',
        'list_': ['Artur', 'Django', 'Python']
    }
    return render(request, 'index.html', context=dict_)