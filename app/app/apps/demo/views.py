from django.shortcuts import render_to_response

def home(request):
	return render_to_response('index.html')
def cadena(request):
	return render_to_response('cadena.html')
def tienda(request):
	return render_to_response('tienda.html')