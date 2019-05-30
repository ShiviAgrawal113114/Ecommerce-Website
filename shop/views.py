from django.shortcuts import render
from django.http import HttpResponse
from.models import Product, Contact
from math import ceil
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
	products = Product.objects.all()
	# print(products)
	n= len(products)
	nSlides = n//4 + ceil((n//4) - (n/4))
	params = {'product': products, 'nSlides': nSlides}
	return render(request, 'shop/index.html', params)

def about(request):
	return render(request, 'shop/about.html')

def contact(request):
	if request.method=="POST":
		name = request.POST.get('name', '')
		email = request.POST.get('email', '')
		phone = request.POST.get('phone', '')
		desc = request.POST.get('desc', '')
		contact = Contact(name=name, email=email, phone=phone, desc=desc)
		con = Contact.objects.values('email', 'desc')
		for i in range(con.count()):
			if(con[i]['email'] == email and con[i]['desc'] == desc):
				return HttpResponse('<script> alert("Duplicate Entry"); </script>')
				break
		contact.save()
	return render(request, 'shop/contact.html')   #how to return to page with alert, login, register, validation, seed factory


def tracker(request):
	return render(request, 'shop/index.html')

def search(request):
	return render(request, 'shop/index.html')

def productView(request):
	return render(request, 'shop/productView.html')

def checkout(request):
	return render(request, 'shop/index.html')

def cart_items(request):
	return render(request, 'shop/cart_items.html')


