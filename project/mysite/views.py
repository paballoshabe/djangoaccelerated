from django.shortcuts import render
from mysite.models import Product, Customer
from . import forms
 
def index(request):
    return render(request, "mysite/index.html")
 
# Create your views here.
def shopping_detail(request):
    customer = Customer.objects.all
    my_dict = {'customers' : customer}
    return render(request, "mysite/shopping_detail.html", context = my_dict)
 
def form_name_view(request):
    form = forms.CustomerForm()
    if request.method == 'POST':
        form = forms.CustomerForm(request.POST)
        if form.is_valid:
            form.save(commit=True)
            return shopping_detail(request)
        else:
            print('Invalid form')
    return render(request, 'mysite/form.html', {'form':form})
 