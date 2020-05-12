from django.shortcuts import render
from django.http import HttpResponse
from my_app.models import Topic, Webpage, AccessRecord, Name
# Create your views here.


def home(request):

    name_list = Name.objects.order_by('first_name')
    my_dict = {'hello_home':name_list}
    return render(request,'my_app/home.htm',context= my_dict)

def product(pro):
    return render(pro,'my_app/product.htm')

def customer(cus):
    return render(cus,'my_app/customer.htm')









