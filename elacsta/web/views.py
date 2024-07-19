from django.shortcuts import render,redirect
from .models import images,event,Registration
from web import RegistrationForm
# Create your views here.


def index(request):
    image=images.objects.all()
    p=event.objects.all()
    context = {
        'image': image,
        'p': p,
    }
    return render(request,'index.html',context)
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
def success(request):
    return render(request,'success.html')
def form(request):
    return render(request,'form.html')
