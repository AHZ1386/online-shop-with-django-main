from  django.shortcuts import render
from django.http import HttpResponse
from Store.models import Category,Product


def test(request):
    context = {
        'category1':Category.objects.get(pk=1),
        'category2':Category.objects.get(pk=2),
        'category3':Category.objects.get(pk=3),

        'last_three_items':Product.objects.order_by('-id')[:3][::-1]

    }
    

    return render(request,'Pages/index.html',context)

