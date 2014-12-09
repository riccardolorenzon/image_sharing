from django.shortcuts import render,redirect

# Create your views here.
from models import sharedimage

def index(request):
    images = sharedimage.objecs.all()
    return render(request, 'index.html', {'images': images})

def handle_upload(request):
    new_sharedimage = sharedimage()
    new_sharedimage.image = request.FILES['file']
    new_sharedimage.title = request.POST['title']
    new_sharedimage.description = request.POST['description']
    new_sharedimage.save()
    redirect('main')