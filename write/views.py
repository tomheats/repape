from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Write
from django.utils import timezone
from django.contrib.auth.models import User


def home(request):
    writes = Write.objects
    all_user = User.objects.all
    all_blogs = Write.objects.all()
    search_term = ''

    if "search" in request.GET:
        search_term = request.GET['search']
        all_blogs = all_blogs.filter(body__icontains=search_term)
    return render(request, 'write/home.html', {'writes': writes, 'name': request.user.username, 'all_user': all_user, 'search_term': search_term, 'all_blogs': all_blogs})


def accounts(request):
    all_user = User.objects.all()
    return render(request, 'accounts/profile.html', {'all_user': all_user})


@login_required
def create(request):
    if request.method == "POST":
        if request.POST['title'] and request.POST['body'] and request.FILES['image'] and request.POST['category']:
            write = Write()
            write.title = request.POST['title']
            write.body = request.POST['body']
            write.image = request.FILES['image']
            write.category = request.POST['category']
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
