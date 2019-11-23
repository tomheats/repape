from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Write
from django.utils import timezone


@login_required
def create(request):
    if request.method == "POST":
        if request.POST['title'] and request.POST['body'] and request.FILES['image']:
            write = Write()
            write.title = request.POST['title']
            write.body = request.POST['body']
            write.image = request.FILES['image']
            write.pub_date = timezone.datetime.now()
            write.writer = request.user
            write.save()
            return redirect('home')
        else:
            return render(request, 'write/create.html', {'error': 'Please fill out all fields.'})
    else:
        return render(request, 'write/create.html')


def detail(request, write_id):
    return render(request, 'write/detail.html')
