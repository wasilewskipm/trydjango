from django.shortcuts import render
from .models import Product


# Create your views here.
def product_detail_view(request):
	obj = Product.objects.get(id=1)
	context = {
		'title': 'Product',
		'object': obj
	}
	return render(request, "product_detail.html", context)