from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Write
from django.utils import timezone


def home(request):
    writes = Write.objects
    return render(request, 'write/home.html', {'writes': writes})


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
            return redirect('/write/' + str(write.id))
        else:
            return render(request, 'write/create.html', {'error': 'Please fill out all fields.'})
    else:
        return render(request, 'write/create.html')


def detail(request, write_id):
    write = get_object_or_404(Write, pk=write_id)
    return render(request, 'write/detail.html', {'write': write})


@login_required
def upvote(request, write_id):
    if request.method == "POST":
        write = get_object_or_404(Write, pk=write_id)
        write.upvotes_total += 1
        write.save()
        return redirect('/write/' + str(write.id))
