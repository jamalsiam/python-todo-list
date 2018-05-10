from django.shortcuts import render, redirect
from .form import dataForm
from .models import Address

def index(request):
    data = Address.objects.order_by('-data_added')
    return render(request,'list/index.html',{'data': data})


def sign(request):
    if request.method == 'POST':
        f = dataForm(request.POST)
        if f.is_valid():
            newRecord = Address(name = request.POST['name'], location = request.POST['location'] )
            newRecord.save()
            return redirect('index')
    else:
        f =dataForm()

        
    context ={'form': f}
    return render(request,'list/sign.html',context)