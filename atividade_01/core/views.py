from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'index.html')

def nome(request):
    return render(request, 'nomes.html')

def campus(request):
    return render(request, 'campus.html')