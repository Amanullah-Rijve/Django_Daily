from django.shortcuts import render, redirect
from .forms import regform

def register(request):
    
    if request.method == 'POST':
        form = regform(request.POST)
        if form.is_valid():
            return redirect('register')
    else:
        form = regform()
    
    return render(request, 'register.html',{'form':form})
