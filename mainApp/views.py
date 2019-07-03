from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'mainApp/homePage.html')

def contact(request):
	return render(request, 'mainApp/basic.html', {'values':['My phone','89498789456','mail@mail.ru']})