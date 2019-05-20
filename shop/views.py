from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	# return HttpResponse("Hey! You Are in Shop.")
	return render(request, 'shop/index.html')

def about(request):
	return render(request, 'shop/about.html')

def contact(request):
	return render(request, 'shop/index.html')

def tracker(request):
	return render(request, 'shop/index.html')

def search(request):
	return render(request, 'shop/index.html')

def productView(request):
	return render(request, 'shop/productView.html')

def checkout(request):
	return render(request, 'shop/index.html')
